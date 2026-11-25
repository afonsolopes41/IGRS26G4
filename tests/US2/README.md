# Testes da US2 – Registo e deregisto

Ambiente: `docker compose up -d` na raiz do repositório; terminal Twinkle da Maria (`maria@acme.operador`); captura com EdgeShark na interface `eth0` do contentor `kamailio`, filtro `sip`. Base de dados de registos verificada com `docker exec kamailio kamcmd ul.dump`.

| # | Teste | Passos | Resultado esperado | Resultado obtido | Captura |
| --- | --- | --- | --- | --- | --- |
| 1 | Registo | Maria → Registration → Register | REGISTER (expires=3600) → 200 OK; `ul.dump` mostra `maria@acme.operador` | ✅ 200 OK; `ul.dump`: AoR `maria@acme.operador`, Records: 1 | `us2_registo.pcapng` |
| 2 | Refresh | Maria já registada → Register (3 vezes) | Cada REGISTER → 200 OK; Expires renovado | ✅ 3 × 200 OK (CSeq 586, 587, 588) | `us2_refresh.pcapng` |
| 3 | Deregisto | Maria registada → Deregister | REGISTER (expires=0) → 200 OK; `ul.dump` sem registos | ✅ 200 OK (CSeq 591); `ul.dump`: Records: 0 | `us2_deregisto.pcapng` |
| 4 | Deregisto sem registo | Maria → Register → Deregister → Deregister outra vez | 2.º deregisto → 404 Not Found | ✅ 200 OK (CSeq 595), 200 OK (CSeq 596), **404 Not Found** (CSeq 597) | `us2_deregisto_404.pcapng` |

Diagramas e mensagens F1..F8: [`docs/sprint1/US2/`](../../docs/sprint1/US2/README.md).

## Base de dados de registos (`ul.dump`)

Depois do teste 1:
```
AoRs: {
    Info: {
        AoR: maria@acme.operador
        Contacts: {
            Contact: {
                Address: sip:maria@172.20.0.2:5090
                Expires: 3598
                Call-ID: skeeszycczdxhvh@terminal.maria
                User-Agent: Twinkle/1.11.0-devel
            }
        }
    }
}
Stats: { Records: 1 }
```

Depois do teste 3:
```
AoRs: { }
Stats: { Records: 0 }
```
