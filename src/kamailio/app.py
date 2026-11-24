# ConferenceControl 2.0 — IGRS 2026/27 Grupo 4
# Lógica do serviço em Python (KEMI). Baseado no script do Laboratório 5.
# Cada user story acrescenta código na rota do seu método SIP.

import os
import KSR as KSR
from aux_classes import RedisDB   # do Lab 5: persistência em Redis (US14)

# --- Constantes (confirmar com o professor) ---
DOMAIN = os.getenv("SIP_DOMAIN") or "acme.operador"
LEADER_AOR = "sip:leader@acme.operador"      # AoR do team leader
CONF_HOST = "sems:5050"                      # servidor de conferências SEMS (Lab 5)


def mod_init():
    KSR.info("===== ConferenceControl 2.0: mod_init\n")
    return kamailio()


class kamailio:
    def __init__(self):
        KSR.info("===== ConferenceControl 2.0: init (domínio %s)\n" % DOMAIN)
        self.db = RedisDB("sipnet.redis")

    def child_init(self, rank):
        return 0

    # --- Rota principal: despacha por método SIP ---
    def ksr_request_route(self, msg):
        if KSR.maxfwd.process_maxfwd(10) < 0:
            reply(483, "Too Many Hops")
            return 1

        # Pedidos dentro de um diálogo (BYE, ACK, re-INVITE)
        if KSR.siputils.has_totag() > 0:
            return self.route_in_dialog(msg)

        if msg.Method == "CANCEL":
            if KSR.tm.t_check_trans() > 0:
                KSR.tm.t_relay()
            return 1
        if msg.Method == "REGISTER":
            return self.route_register(msg)
        if msg.Method == "INVITE":
            return self.route_invite(msg)
        if msg.Method == "MESSAGE":
            return self.route_message(msg)

        reply(405, "Method Not Allowed")
        return 1

    # --- Pedidos dentro de um diálogo ---
    def route_in_dialog(self, msg):
        if KSR.rr.loose_route() > 0:
            KSR.tm.t_relay()
            return 1
        if msg.Method == "ACK":
            if KSR.tm.t_check_trans() > 0:
                KSR.tm.t_relay()
            return 1
        reply(404, "Not Here")
        return 1

   # --- REGISTER: US1 (Rafael Reis) e US2 (Afonso) ---
    def route_register(self, msg):
        # US1: Rejeitar domínios que não sejam acme.operador
        domain = pv("$rd")
        if not is_acme(domain):
            reply(403, "Forbidden")
            return 1

        # US2: registo/deregisto com 404 (a implementar)
        KSR.registrar.save("location", 0)   
        return 1

    # --- INVITE: US3, US5, US6, US7, US8, US9 ---
    def route_invite(self, msg):
        # US5/US7: pedidos para common@ e team@ (a implementar, com forward_to_conference)
        if KSR.registrar.lookup("location") < 0:
            reply(404, "Not Found")
            return 1
        KSR.rr.record_route()
        KSR.tm.t_relay()
        return 1

    # --- MESSAGE: US4 (PIN) e US10 (# / * do leader) ---
    def route_message(self, msg):
        # US4: validar@ (a implementar)
        if (pv("$rb").strip() != "0000" or not is_acme(pv("$fd"))):
            reply(403, "Forbidden")
            return 1
        else:
            KSR.pv.sets("$sht(valid=>$fu)", "1")
            reply(200, "OK")
            return 1
        # US10: resposta do leader (a implementar)
        if KSR.registrar.lookup("location") < 0:
            reply(404, "Not Found")
            return 1
        KSR.tm.t_relay()
        return 1

    def ksr_reply_route(self, msg):
        return 1

    def ksr_onsend_route(self, msg):
        return 1

    def ksr_failure_route_INVITE(self, msg):
        # US11: falhas do servidor de conferências (408/5xx) contam como KPI
        return 1


# --- Helpers partilhados pelo grupo ---

def pv(name):
    """Lê uma pseudo-variável do Kamailio (ex.: pv("$fd")); devolve "" se não existir."""
    value = KSR.pv.get(name)
    return value if value is not None else ""


def is_acme(domain):
    """True se o domínio for o do operador ACME."""
    return domain == DOMAIN


def reply(code, reason):
    """Responde sem estado (stateless) ao pedido atual."""
    KSR.sl.send_reply(code, reason)


def forward_to_conference(room):
    """Encaminha o pedido atual para a sala `room` do SEMS (ex.: "common", "team")."""
    KSR.pv.sets("$ru", "sip:%s@%s" % (room, CONF_HOST))
    KSR.rr.record_route()
    KSR.tm.t_relay()
