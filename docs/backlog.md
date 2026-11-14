# Product Backlog — ConferenceControl 2.0

Story points em escala de Fibonacci (1, 2, 3, 5, 8). Derivado dos requisitos do serviço (§2 do enunciado) e do modelo GRL (`docs/grl/`).

## Epics

| Epic | Descrição |
| --- | --- |
| E1 | Serviços básicos (registo, chamadas, acesso) |
| E2 | Sala de conferências comum |
| E3 | Sala de conferências da equipa |
| E4 | Monitorização (KPIs, YANG, gNMI) |

## User stories

| US | Epic | Como… | Quero… | Para… | SP | Sprint | Responsável |
| --- | --- | --- | --- | --- | --- | --- | --- |
| US1 | E1 | Operador | rejeitar registos de domínios diferentes de acme.operador (403) | garantir que só assinantes acedem ao serviço | 1 | 1 | Rafael Reis |
| US2 | E1 | Colaborador | registar-me e deregistar-me em acme.operador | poder usar o ConferenceControl 2.0 | 2 | 1 | Afonso Lopes |
| US3 | E1 | Colaborador | estabelecer e terminar chamadas de voz com colegas | comunicar com a equipa | 3 | 1 | Rafael Reis |
| US4 | E1 | Colaborador | validar o meu acesso com um PIN enviado por SIP MESSAGE | aceder ao serviço de forma segura | 3 | 1 | Rafael Silva |
| US5 | E2 | Colaborador | entrar e sair da sala de conferências comum | participar em reuniões abertas | 2 | 1 | Gonçalo Batista |
| US6 | E1/E2 | Operador | recusar (403) qualquer pedido de utilizadores de outros domínios | proteger o serviço | 1 | 1 | Rafael Reis |
| US7 | E3 | Team leader | abrir e fechar a sala de equipa | controlar quando a equipa reúne | 3 | 2 | Rafael Reis |
| US8 | E3 | Colaborador | ser informado de que a sala de equipa está fechada | tentar mais tarde | 2 | 2 | Rafael Reis |
| US9 | E3 | Team leader | ser notificado (MESSAGE) de pedidos de acesso à sala de equipa | decidir quem entra | 8 | 2 | Afonso Lopes |
| US10 | E3 | Team leader | aceitar (#) ou rejeitar (*) os pedidos de acesso | gerir a equipa de forma eficiente | 5 | 2 | Afonso Lopes |
| US11 | E4 | Operador | contar KPIs (conferências efetuadas, falhadas, …) | monitorizar o desempenho do serviço | 3 | 3 | Gonçalo Batista |
| US12 | E4 | Operador | ter a especificação YANG dos KPIs | documentar as métricas de forma standard | 3 | 2 | Rafael Silva |
| US13 | E4 | Operador | consultar os KPIs por gNMI | aceder às métricas por uma interface standard | 8 | 3 | Rafael Silva |
| US14 | E4 | Operador | guardar os KPIs de forma persistente e não persistente | não perder métricas e consultá-las rapidamente | 3 | 3 | Gonçalo Batista |

**Total:** 47 story points.
