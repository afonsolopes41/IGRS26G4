# IGRS 2026/27 — Grupo 4 — ConferenceControl 2.0

Trabalho prático da UC Inteligência e Gestão de Redes e Serviços (ISCTE): especificação, criação e implementação de um serviço suplementar de telecomunicações baseado em SIP e gNMI, desenvolvido com Scrum.

## Grupo

| Nome | Número |
| --- | --- |
| Afonso Lopes | 122631 |
| Gonçalo Batista | 122623 |
| Rafael Reis | 122616 |
| Rafael Silva | 122638 |

## Estrutura do repositório

| Pasta | Conteúdo |
| --- | --- |
| `docs/grl/` | Modelo GRL (ficheiro fonte + imagem) |
| `docs/backlog.md` | Product Backlog (user stories e story points) |
| `docs/sprint1/`, `docs/sprint2/`, `docs/sprint3/` | Sprint Backlog, Definition of Ready/Done, diagramas e Increment de cada sprint |
| `src/kamailio/` | Configuração do Kamailio e scripts Python (KEMI) |
| `src/gnmi/` | Modelo YANG e servidor gNMI dos KPIs |
| `tests/` | Testes por user story (`tests/USx/`): descrição + capturas `.pcapng` |

## Convenções

- Cada commit começa pela user story: `[US2] feat: ...`, `[US2] docs: ...`, `[US2] test: ...`.
- Trabalho em branches `feature/USx-descricao` e entrada no `main` por Pull Request.
- Planeamento e reuniões no Trello (board `IGRS26G4`), com links para os commits.

## Como executar
1. Construir as imagens dos labs: `kamailio:igrs_2026` e `sems:igrs_2026` (dockerfiles em `docker/`) e `twinkle:igrs_2026` (Lab 2).
2. Na raiz do repositório: `docker compose up -d`
3. Verificar o Kamailio: `docker logs kamailio` (deve mostrar `ConferenceControl 2.0: init`).
4. Abrir os Twinkle (Leader, Maria, Joao, Manel) e registar.
5. Ver os registos: `docker exec kamailio kamcmd ul.dump`

## Onde escrever cada user story

| Função em `src/kamailio/app.py` | User stories |
| --- | --- |
| `route_register` | US1, US2 |
| `route_invite` | US3, US5, US6, US7, US8, US9 |
| `route_message` | US4, US10 |
| `ksr_failure_route_INVITE` | US11 |

Estado partilhado (salas, pedidos, KPIs) vai para `htable` (ver `kamailio.cfg`), nunca para variáveis Python globais. KPIs persistentes vão para o Redis (`aux_classes.RedisDB`).)
