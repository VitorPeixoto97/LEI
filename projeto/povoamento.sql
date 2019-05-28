INSERT INTO "public"."server_clube" ("id", "nome", "cor", "simbolo") VALUES ('1', 'FC Porto', '#0F579E', 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/FC_Porto.svg/1200px-FC_Porto.svg.png'),
('2', 'SL Benfica', '#EF2F22', 'https://www.zerozero.pt/img/logos/equipas/4_imgbank.png'),
('3', 'Sporting CP', '#1B6F47', 'https://seeklogo.com/images/S/sporting-lisbon-sporting-clube-de-portugal-logo-87718592BF-seeklogo.com.png'),
('4', 'UD Oliveirense', '#E0241E', 'https://www.zerozero.pt/img/logos/equipas/2199_imgbank.png'),
('5', 'OC Barcelos', '#2A1B70', 'https://www.zerozero.pt/img/logos/equipas/209914_imgbank.png'),
('6', 'Juventude Viana', '#FF7500', 'https://www.zerozero.pt/img/logos/equipas/209908_imgbank.png'),
('7', 'Riba D''Ave HC', '#E0241E', 'https://www.zerozero.pt/img/logos/equipas/209915_imgbank.png'),
('8', 'HC Braga', '#0F579E', 'https://www.zerozero.pt/img/logos/equipas/210065_imgbank.png'),
('9', 'HC Turquel', '#111111', 'https://www.zerozero.pt/img/logos/equipas/209898_imgbank.png'),
('10', 'AD Valongo', '#3B6F47', 'https://www.zerozero.pt/img/logos/equipas/209909_imgbank.png'),
('11', 'Paço de Arcos', '#0F379E', 'https://www.zerozero.pt/img/logos/equipas/209911_imgbank.png'),
('12', 'AD Oeiras', '#EF2F22', 'https://www.zerozero.pt/img/logos/equipas/3936_imgbank.png'),
('13', 'SC Tomar', '#6BA122', 'https://www.zerozero.pt/img/logos/equipas/58074_imgbank.png'),
('14', 'SC Marinhense', '#00713C', 'https://www.zerozero.pt/img/logos/equipas/214133_imgbank.png'),
('15', 'FC Barcelona', '#7F001F', 'http://pngimg.com/uploads/fcb_logo/fcb_logo_PNG25.png');

INSERT INTO "public"."server_formacao" ("id", "nome", "clube_id") VALUES ('1', 'Séniores', '1'),
('2', 'Séniores', '2'),
('3', 'Séniores', '3'),
('4', 'Séniores', '4'),
('5', 'Séniores', '5'),
('6', 'Séniores', '6'),
('7', 'Séniores', '7'),
('8', 'Séniores', '8'),
('9', 'Séniores', '9'),
('10', 'Séniores', '10'),
('11', 'Séniores', '11'),
('12', 'Séniores', '12'),
('13', 'Séniores', '13'),
('14', 'Séniores', '14'),
('15', 'Séniores', '15');

INSERT INTO "public"."server_jogo" ("id", "tipo", "casa", "data", "hora", "grelhaCampo", "grelhaBaliza", "adversario_id", "formacao_id", "numero", "ativo") VALUES ('0', 'Competição', 'f', '2019-04-27', '17:00:00', '8x4', '3x3', '5', '1', '0', 't'),
('1', 'Competição', 'f', '2019-05-04', '19:30:00', '8x4', '3x3', '3', '1', '1', 't'),
('2', 'Competição', 'f', '2019-05-11', '12:00:00', '8x4', '3x3', '15', '1', '2', 't'),
('3', 'Competição', 't', '2019-05-15', '21:00:00', '8x4', '3x3', '7', '1', '3', 't'),
('4', 'Competição', 'f', '2019-05-19', '16:00:00', '8x4', '3x3', '10', '1', '4', 't'),
('5', 'Competição', 't', '2019-05-25', '18:00:00', '8x4', '3x3', '9', '1', '5', 't'),
('6', 'Competição', 't', '2019-03-16', '17:00:00', '8x4', '3x3', '3', '1', '6', 'f');

INSERT INTO "public"."server_tecnico" ("id", "email", "grelhaCampo", "grelhaBaliza", "clube_id") VALUES ('0', 'a79175@alunos.uminho.pt', '8x4', '3x3', '1');

INSERT INTO "public"."server_atleta" ("id", "nome", "licenca", "camisola", "formacao_id") VALUES ('0', 'Gonçalo Alves', '0', '77', '1'),
('1', 'Poka', '1', '18', '1'),
('2', 'Reinaldo García', '2', '57', '1'),
('3', 'Matías Platero', '3', '7', '3');

INSERT INTO "public"."server_tipoevento" ("id", "tipo", "atleta1", "atleta2", "zonaCampo", "zonaBaliza", "novoinstante", "equipa") VALUES ('0', 'Golo', 't', 'f', 't', 't', 'f', 't'),
('1', 'Remate à baliza', 't', 'f', 't', 't', 'f', 't'),
('2', 'Remate intercetado', 't', 'f', 't', 'f', 'f', 't'),
('3', 'Remate fora', 't', 'f', 't', 'f', 'f', 't'),
('4', 'Substituição', 't', 't', 'f', 'f', 'f', 't');

INSERT INTO "public"."server_tiposselecionados" ("id", "tecnico_id", "tipo_id") VALUES ('1', '0', '0');

INSERT INTO "public"."server_convocado" ("id", "emCampo", "atleta_id", "jogo_id") VALUES ('1', 't', '0', '5'),
('2', 't', '1', '5'),
('3', 'f', '2', '5');

INSERT INTO "public"."server_evento" ("id", "zonaCampo", "zonaBaliza", "instante", "novoinstante", "timestamp", "atleta1_id", "atleta2_id", "equipa_id", "jogo_id", "tipo_id") VALUES ('0', '6', '9', '00:05:12', NULL, '2019-03-16 17:05:14.347796+00', '0', NULL, '1', '6', '0'),
('1', '11', '9', '00:08:50', NULL, '2019-03-16 17:08:52.347796+00', '1', NULL, '1', '6', '0'),
('2', '7', '3', '00:30:36', NULL, '2019-03-16 17:40:36.347796+00', '2', NULL, '1', '6', '0'),
('3', '26', '9', '00:21:21', NULL, '2019-03-16 17:21:23.347796+00', '3', NULL, '3', '6', '0'),
('4', '10', '3', '00:32:12', NULL, '2019-03-16 17:42:23.347796+00', '2', NULL, '1', '6', '1'),
('5', '6', NULL, '00:35:12', NULL, '2019-03-16 17:45:23.347796+00', '0', NULL, '1', '6', '2'),
('6', NULL, NULL, '00:26:31', NULL, '2019-03-16 17:36:23.347796+00', '1', '2', '1', '6', '4'),
('7', '6', NULL, '00:22:12', NULL, '2019-05-25 19:32:23.347796+01', '0', NULL, '1', '5', '2');





