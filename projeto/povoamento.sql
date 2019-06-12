INSERT INTO "public"."auth_group" ("id", "name") VALUES ('2', 'Administrador'),
('3', 'Gestor'),
('4', 'Tecnico');

INSERT INTO "public"."auth_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES ('1', 'pbkdf2_sha256$150000$QUvpelrwAw7r$5HPQvgbVxeKrMNZIdpuB1d+nEZELBgq/ETJIdsopsTs=', '2019-05-08 10:57:14.273069+01', 't', 'admin@alunos.uminho.pt', '', '', 'admin@alunos.uminho.pt', 't', 't', '2019-04-10 19:22:09.457293+01'),
('4', 'pbkdf2_sha256$150000$avHO5ClLaaTq$pgcBGWBIxCcnYS8ca0SaykMAo6cbIq+AP2xIKvhS/ks=', NULL, 'f', 'a75281@alunos.uminho.pt', 'Salete', 'Teixeira', 'a75281@alunos.uminho.pt', 'f', 't', '2019-04-27 19:15:18+01'),
('5', 'pbkdf2_sha256$150000$aDR8TPo3LfI8$+oZktFupyv9MEpf1POz1HnBwk4zlq0sVpLHMoQvVTJk=', NULL, 'f', 'a77531@alunos.uminho.pt', 'Daniel', 'Maia', 'a77531@alunos.uminho.pt', 'f', 't', '2019-04-27 19:16:31+01'),
('6', 'pbkdf2_sha256$150000$GVbYWFIMaCO2$4vZPAYsLFdd1BNh6CoLCqSQ44L5eS/gVGsIVe9Zai1s=', '2019-04-27 23:57:57.226051+01', 'f', 'a79175@alunos.uminho.pt', 'Vitor', 'Peixoto', 'a79175@alunos.uminho.pt', 'f', 't', '2019-04-27 19:17:15+01');

INSERT INTO "public"."auth_user_groups" ("id", "user_id", "group_id") VALUES ('3', '4', '2'),
('4', '5', '3'),
('5', '6', '4');

INSERT INTO "public"."auth_group_permissions" ("id", "group_id", "permission_id") VALUES ('9', '2', '41'),
('10', '2', '13'),
('11', '2', '53'),
('12', '2', '56'),
('13', '2', '58'),
('14', '2', '60'),
('15', '3', '25'),
('16', '3', '26'),
('17', '3', '27'),
('18', '3', '28'),
('19', '3', '29'),
('20', '3', '30'),
('21', '3', '31'),
('22', '3', '32'),
('23', '3', '33'),
('24', '3', '34'),
('25', '3', '35'),
('26', '3', '36'),
('27', '3', '37'),
('28', '3', '38'),
('29', '3', '39'),
('30', '3', '40'),
('31', '3', '41'),
('32', '3', '44'),
('33', '3', '48'),
('34', '3', '49'),
('35', '3', '50'),
('36', '3', '51'),
('37', '3', '52'),
('38', '3', '54'),
('39', '3', '56'),
('40', '3', '64'),
('41', '4', '32'),
('42', '4', '64'),
('43', '4', '65'),
('44', '4', '66'),
('46', '4', '37'),
('47', '4', '38'),
('48', '4', '39'),
('49', '4', '40'),
('50', '4', '67'),
('51', '4', '68'),
('52', '4', '45'),
('53', '4', '46'),
('54', '4', '47'),
('55', '4', '48'),
('56', '4', '50'),
('57', '4', '52'),
('58', '4', '56'),
('59', '4', '61');

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

INSERT INTO "public"."server_jogo" ("id", "tipo", "casa", "data", "hora", "grelhaCampo", "grelhaBaliza", "adversario_id", "formacao_id", "numero", "ativo", "duracao", "partes") VALUES 
('0', 'Competição', 'f', '2019-04-27', '17:00:00', '8x4', '3x3', '5', '1', '0', 't', '20', '2'),
('1', 'Competição', 'f', '2019-05-04', '19:30:00', '8x4', '3x3', '3', '1', '1', 't', '20', '2'),
('2', 'Competição', 'f', '2019-05-11', '12:00:00', '8x4', '3x3', '15', '1', '2', 't', '20', '2'),
('3', 'Competição', 't', '2019-05-15', '21:00:00', '8x4', '3x3', '7', '1', '3', 't', '20', '2'),
('4', 'Competição', 'f', '2019-05-19', '16:00:00', '8x4', '3x3', '10', '1', '4', 't', '20', '2'),
('5', 'Competição', 't', '2019-05-25', '18:00:00', '8x4', '3x3', '9', '1', '5', 't', '10', '4'),
('6', 'Competição', 't', '2019-03-16', '17:00:00', '8x4', '3x3', '3', '1', '6', 'f', '20', '2');

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

INSERT INTO "public"."server_evento" ("id", "zonaCampo", "zonaBaliza", "instante", "novoinstante", "timestamp", "atleta1_id", "atleta2_id", "equipa_id", "jogo_id", "tipo_id", "parte", "sinalizado") VALUES 
('0', '6', '9', '00:05:12', NULL, '2019-03-16 17:05:14.347796+00', '0', NULL, '1', '6', '0', '1', 't'),
('1', '11', '9', '00:08:50', NULL, '2019-03-16 17:08:52.347796+00', '1', NULL, '1', '6', '0', '1', 'f'),
('2', '7', '3', '00:30:36', NULL, '2019-03-16 17:40:36.347796+00', '2', NULL, '1', '6', '0', '1', 't'),
('3', '26', '9', '00:21:21', NULL, '2019-03-16 17:21:23.347796+00', '3', NULL, '3', '6', '0', '1', 't'),
('4', '10', '3', '00:32:12', NULL, '2019-03-16 17:42:23.347796+00', '2', NULL, '1', '6', '1', '1', 'f'),
('5', '6', NULL, '00:35:12', NULL, '2019-03-16 17:45:23.347796+00', '0', NULL, '1', '6', '2', '1', 'f'),
('6', NULL, NULL, '00:26:31', NULL, '2019-03-16 17:36:23.347796+00', '1', '2', '1', '6', '4', '1', 'f'),
('7', '6', NULL, '00:22:12', NULL, '2019-05-25 19:32:23.347796+01', '0', NULL, '1', '5', '2', '1', 'f');





