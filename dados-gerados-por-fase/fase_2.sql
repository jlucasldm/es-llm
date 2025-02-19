-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.0.40 - MySQL Community Server - GPL
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando dados para a tabela weyes.caso_teste: ~149 rows (aproximadamente)
INSERT IGNORE INTO `caso_teste` (`id`, `questao_id`, `entrada`, `saida`, `created_at`, `updated_at`, `validation_status`, `validated_result`) VALUES
	(1, 1, '1 1', '1', '2024-12-22 15:33:34.243782', '2024-12-22 15:33:34.243782', 'PASSED', '1'),
	(2, 1, '10 2', '5', '2024-12-22 15:33:34.251335', '2024-12-22 15:33:34.251335', 'PASSED', '5'),
	(3, 1, '50 5', '10', '2024-12-22 15:33:34.252299', '2024-12-22 15:33:34.252299', 'PASSED', '10'),
	(4, 1, '200 4', '50', '2024-12-22 15:33:34.252299', '2024-12-22 15:33:34.252299', 'PASSED', '50'),
	(5, 1, '250 5', '50', '2024-12-22 15:33:34.253301', '2024-12-22 15:33:34.253301', 'PASSED', '50'),
	(6, 1, '300 6', '50', '2024-12-22 15:33:34.253301', '2024-12-22 15:33:34.253301', 'PASSED', '50'),
	(7, 1, '400 8', '50', '2024-12-22 15:33:34.254304', '2024-12-22 15:33:34.254304', 'PASSED', '50'),
	(8, 1, '500 10', '50', '2024-12-22 15:33:34.255305', '2024-12-22 15:33:34.255305', 'PASSED', '50'),
	(9, 1, '450 9', '50', '2024-12-22 15:33:34.255305', '2024-12-22 15:33:34.255305', 'PASSED', '50'),
	(10, 1, '100 1', '100', '2024-12-22 15:33:34.256303', '2024-12-22 15:33:34.256303', 'PASSED', '100'),
	(11, 1, '500 1', '500', '2024-12-22 15:33:34.256821', '2024-12-22 15:33:34.256821', 'PASSED', '500'),
	(12, 1, '499 100', '4', '2024-12-22 15:33:34.256821', '2024-12-22 15:33:34.256821', 'PASSED', '4'),
	(13, 1, '250 100', '2', '2024-12-22 15:33:34.257835', '2024-12-22 15:33:34.257835', 'PASSED', '2'),
	(14, 1, '1 100', '0', '2024-12-22 15:33:34.257835', '2024-12-22 15:33:34.257835', 'PASSED', '0'),
	(15, 1, '500 100', '5', '2024-12-22 15:33:34.258851', '2024-12-22 15:33:34.258851', 'PASSED', '5'),
	(16, 2, '1 1 1 1 1 1', '6', '2024-12-22 15:33:42.867371', '2024-12-22 15:33:42.867371', 'PASSED', '6'),
	(17, 2, '2 2 2 2 2 2', '12', '2024-12-22 15:33:42.867371', '2024-12-22 15:33:42.867371', 'PASSED', '12'),
	(18, 2, '3 3 3 3 3 3', '18', '2024-12-22 15:33:42.868361', '2024-12-22 15:33:42.868361', 'PASSED', '18'),
	(19, 2, '1 2 3 4 5 6', '21', '2024-12-22 15:33:42.869315', '2024-12-22 15:33:42.869315', 'PASSED', '21'),
	(20, 2, '2 4 6 8 10 12', '42', '2024-12-22 15:33:42.869315', '2024-12-22 15:33:42.869315', 'PASSED', '42'),
	(21, 2, '1 3 5 7 9 10', '35', '2024-12-22 15:33:42.870362', '2024-12-22 15:33:42.870362', 'PASSED', '35'),
	(22, 2, '10 10 10 10 10 10', '60', '2024-12-22 15:33:42.871325', '2024-12-22 15:33:42.871325', 'PASSED', '60'),
	(23, 2, '5 5 5 5 5 5', '30', '2024-12-22 15:33:42.871325', '2024-12-22 15:33:42.871325', 'PASSED', '30'),
	(24, 2, '1 2 1 2 1 2', '9', '2024-12-22 15:33:42.872331', '2024-12-22 15:33:42.872331', 'PASSED', '9'),
	(25, 2, '10 9 8 7 6 5', '45', '2024-12-22 15:33:42.873365', '2024-12-22 15:33:42.873365', 'PASSED', '45'),
	(26, 2, '10 10 10 10 10 1', '61', '2024-12-22 15:33:42.873365', '2024-12-22 15:33:42.873365', 'FAILED', '51'),
	(27, 2, '1 1 1 1 1 10', '15', '2024-12-22 15:33:42.874316', '2024-12-22 15:33:42.874316', 'PASSED', '15'),
	(28, 2, '10 9 10 9 10 9', '57', '2024-12-22 15:33:42.875321', '2024-12-22 15:33:42.875321', 'PASSED', '57'),
	(29, 2, '1 1 1 1 1 1', '6', '2024-12-22 15:33:42.876316', '2024-12-22 15:33:42.876316', 'PASSED', '6'),
	(30, 2, '10 10 10 10 10 10', '60', '2024-12-22 15:33:42.876916', '2024-12-22 15:33:42.876916', 'PASSED', '60'),
	(31, 3, '6 6 6\n0 0 0', '18', '2024-12-22 15:33:52.252310', '2024-12-22 15:33:52.252310', 'PASSED', '18'),
	(32, 3, '10 10 10\n1 1 1', '24', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '21'),
	(33, 3, '8 9 10\n0 0 2', '31', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '21'),
	(34, 3, '12 15 18\n2 1 0', '39', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '36'),
	(35, 3, '20 19 18\n0 2 1', '54', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '48'),
	(36, 3, '15 15 15\n1 1 1', '42', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '36'),
	(37, 3, '6 7 8\n2 2 2', '0', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '3'),
	(38, 3, '10 12 20\n0 1 1', '36', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'PASSED', '36'),
	(39, 3, '19 20 18\n0 0 0', '57', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'PASSED', '57'),
	(40, 3, '6 6 6\n0 1 2', '9', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'PASSED', '9'),
	(41, 3, '20 20 20\n2 2 2', '54', '2024-12-22 15:33:52.256321', '2024-12-22 15:33:52.256321', 'FAILED', '42'),
	(42, 3, '10 10 10\n0 0 1', '27', '2024-12-22 15:33:52.266705', '2024-12-22 15:33:52.266705', 'PASSED', '27'),
	(43, 3, '18 19 20\n1 0 0', '55', '2024-12-22 15:33:52.268214', '2024-12-22 15:33:52.268214', 'FAILED', '54'),
	(44, 3, '7 8 9\n1 1 0', '30', '2024-12-22 15:33:52.268214', '2024-12-22 15:33:52.268214', 'FAILED', '18'),
	(45, 3, '20 20 20\n0 1 0', '57', '2024-12-22 15:33:52.268214', '2024-12-22 15:33:52.268214', 'PASSED', '57'),
	(46, 3, '6 6 6\n2 2 0', '12', '2024-12-22 15:33:52.268214', '2024-12-22 15:33:52.268214', 'FAILED', '6'),
	(47, 4, '3 3 3 3', '4', '2024-12-22 15:33:59.948090', '2024-12-22 15:33:59.948090', 'PASSED', '4'),
	(48, 4, '3 4 5 6', '10', '2024-12-22 15:33:59.957475', '2024-12-22 15:33:59.957475', 'PASSED', '10'),
	(49, 4, '5 5 5 5', '12', '2024-12-22 15:33:59.957475', '2024-12-22 15:33:59.957475', 'PASSED', '12'),
	(50, 4, '10 10 10 10', '32', '2024-12-22 15:33:59.957475', '2024-12-22 15:33:59.957475', 'PASSED', '32'),
	(51, 4, '4 4 4 4', '8', '2024-12-22 15:33:59.965169', '2024-12-22 15:33:59.965169', 'PASSED', '8'),
	(52, 4, '6 7 8 9', '22', '2024-12-22 15:33:59.967044', '2024-12-22 15:33:59.967044', 'PASSED', '22'),
	(53, 4, '15 15 15 15', '52', '2024-12-22 15:33:59.967044', '2024-12-22 15:33:59.967044', 'PASSED', '52'),
	(54, 4, '12 13 14 15', '46', '2024-12-22 15:33:59.967044', '2024-12-22 15:33:59.967044', 'PASSED', '46'),
	(55, 4, '20 20 20 20', '76', '2024-12-22 15:33:59.967044', '2024-12-22 15:33:59.967044', 'FAILED', '72'),
	(56, 4, '3 6 9 12', '22', '2024-12-22 15:33:59.967044', '2024-12-22 15:33:59.967044', 'PASSED', '22'),
	(57, 4, '8 8 8 8', '28', '2024-12-22 15:33:59.976676', '2024-12-22 15:33:59.976676', 'FAILED', '24'),
	(58, 4, '7 7 7 7', '20', '2024-12-22 15:33:59.976676', '2024-12-22 15:33:59.976676', 'PASSED', '20'),
	(59, 4, '9 10 11 12', '34', '2024-12-22 15:33:59.976676', '2024-12-22 15:33:59.976676', 'PASSED', '34'),
	(60, 4, '18 19 20 20', '69', '2024-12-22 15:33:59.980240', '2024-12-22 15:33:59.980240', 'PASSED', '69'),
	(61, 4, '4 5 6 7', '14', '2024-12-22 15:33:59.980240', '2024-12-22 15:33:59.980240', 'PASSED', '14'),
	(62, 4, '16 17 18 19', '66', '2024-12-22 15:33:59.980240', '2024-12-22 15:33:59.980240', 'FAILED', '62'),
	(63, 5, '1 1', '0', '2024-12-22 15:34:06.657018', '2024-12-22 15:34:06.657018', 'PASSED', '0'),
	(64, 5, '1 10', '0', '2024-12-22 15:34:06.657018', '2024-12-22 15:34:06.657018', 'PASSED', '0'),
	(65, 5, '10 5', '5', '2024-12-22 15:34:06.657018', '2024-12-22 15:34:06.657018', 'PASSED', '5'),
	(66, 5, '100 250', '50', '2024-12-22 15:34:06.666804', '2024-12-22 15:34:06.666804', 'PASSED', '50'),
	(67, 5, '200 400', '0', '2024-12-22 15:34:06.666960', '2024-12-22 15:34:06.666960', 'PASSED', '0'),
	(68, 5, '500 1000', '0', '2024-12-22 15:34:06.671387', '2024-12-22 15:34:06.671387', 'PASSED', '0'),
	(69, 5, '1000 1500', '500', '2024-12-22 15:34:06.673658', '2024-12-22 15:34:06.673658', 'PASSED', '500'),
	(70, 5, '10000 9999', '9999', '2024-12-22 15:34:06.673658', '2024-12-22 15:34:06.673658', 'PASSED', '9999'),
	(71, 5, '10000 10000', '0', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'PASSED', '0'),
	(72, 5, '9999 10000', '1', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'PASSED', '1'),
	(73, 5, '5000 7500', '2500', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'PASSED', '2500'),
	(74, 5, '3000 6000', '0', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'PASSED', '0'),
	(75, 5, '2500 12500', '500', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'FAILED', '0'),
	(76, 5, '7500 22500', '7500', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'FAILED', '0'),
	(77, 5, '10000 20000', '0', '2024-12-22 15:34:06.676796', '2024-12-22 15:34:06.676796', 'PASSED', '0'),
	(78, 6, '2 3 4 5 6', '20', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'PASSED', '20'),
	(79, 6, '1000000 2000000 3000000 4000000 5000000', '15000000', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'PASSED', '15000000'),
	(80, 6, '100000 200000 300000 400000 500000', '1500000', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'PASSED', '1500000'),
	(81, 6, '999999999 888888888 777777777 666666666 555555555', '3888888883', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'FAILED', '-406078411'),
	(82, 6, '1 1 1 1 1', '5', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'PASSED', '5'),
	(83, 6, '999999998 999999997 999999996 999999995 999999994', '4999999980', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'FAILED', '705032684'),
	(84, 6, '250000000 250000000 250000000 250000000 250000000', '1250000000', '2024-12-22 15:34:15.726880', '2024-12-22 15:34:15.726880', 'PASSED', '1250000000'),
	(85, 6, '500000000 500000000 500000000 500000000 500000000', '2500000000', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'FAILED', '-1794967296'),
	(86, 6, '123456789 987654321 234567890 876543210 345678901', '1567901111', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'FAILED', '-1727066185'),
	(87, 6, '100000000 200000000 300000000 400000000 500000000', '1500000000', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'PASSED', '1500000000'),
	(88, 6, '999999999 1 1 1 1', '100000003', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'FAILED', '1000000003'),
	(89, 6, '500000000 500000000 500000000 500000000 1', '2000000001', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'PASSED', '2000000001'),
	(90, 6, '999999999 999999998 999999997 999999996 999999995', '4999999985', '2024-12-22 15:34:15.731387', '2024-12-22 15:34:15.731387', 'FAILED', '705032689'),
	(91, 6, '100000000 200000000 300000000 400000000 100000000', '1100000000', '2024-12-22 15:34:15.734893', '2024-12-22 15:34:15.734893', 'PASSED', '1100000000'),
	(92, 6, '999999999 999999999 999999999 999999999 999999999', '4999999995', '2024-12-22 15:34:15.734893', '2024-12-22 15:34:15.734893', 'FAILED', '705032699'),
	(93, 7, '1\n Frodo 50\n 50', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(94, 7, '2\n Sam 55\n Merry 60\n 120', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(95, 7, '3\n Pippin 70\n Legolas 80\n Gimli 90\n 200', 'Vamos virar almoço de aranhas gigantes!\n Legolas\n Gimli', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(96, 7, '4\n Boromir 75\n Aragorn 85\n Faramir 70\n Eowyn 60\n 200', 'Vamos virar almoço de aranhas gigantes!\n Boromir\n Aragorn', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(97, 7, '5\n Gollum 50\n Smeagol 55\n Bilbo 60\n Thorin 70\n Dwalin 80\n 250', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(98, 7, '6\n Kili 60\n Fili 65\n Dori 70\n Nori 75\n Ori 80\n Oin 85\n 300', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(99, 7, '7\n Bifur 55\n Bofur 60\n Bombur 65\n Dwalin 70\n Balin 75\n Thorin 80\n Fili 85\n 200', 'Vamos virar almoço de aranhas gigantes!\n Dwalin\n Balin\n Thorin\n Fili', '2024-12-22 15:34:38.506170', '2024-12-22 15:34:38.506170', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(100, 7, '8\n Dori 60\n Nori 65\n Ori 70\n Oin 75\n Gloin 80\n Bifur 85\n Bofur 90\n Bombur 95\n 300', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(101, 7, '9\n Sam 55\n Frodo 50\n Merry 60\n Pippin 70\n Legolas 80\n Gimli 90\n Boromir 75\n Aragorn 85\n Faramir 70\n 250', 'Vamos virar almoço de aranhas gigantes!\n Legolas\n Gimli\n Boromir\n Aragorn', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(102, 7, '10\n Gollum 50\n Smeagol 55\n Bilbo 60\n Thorin 70\n Dwalin 80\n Kili 65\n Fili 75\n Dori 85\n Nori 90\n Ori 95\n 300', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(103, 7, '11\n Oin 70\n Gloin 75\n Bifur 80\n Bofur 85\n Bombur 90\n Dwalin 95\n Balin 100\n Thorin 105\n Fili 110\n Kili 115\n Dori 120\n 250', 'Vamos virar almoço de aranhas gigantes!\n Oin\n Gloin\n Bifur\n Bofur\n Bombur\n Dwalin\n Balin\n Thorin\n Fili\n Kili\n Dori', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(104, 7, '12\n Sam 55\n Frodo 50\n Merry 60\n Pippin 70\n Legolas 80\n Gimli 90\n Boromir 75\n Aragorn 85\n Faramir 70\n Gollum 50\n Smeagol 55\n Bilbo 60\n 300', 'Vamos todos encontrar a montanha!', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'PASSED', 'Vamos todos encontrar a montanha!'),
	(105, 7, '13\n Dori 60\n Nori 65\n Ori 70\n Oin 75\n Gloin 80\n Bifur 85\n Bofur 90\n Bombur 95\n Dwalin 100\n Balin 105\n Thorin 110\n Fili 115\n Kili 120\n 250', 'Vamos virar almoço de aranhas gigantes!\n Dori\n Nori\n Ori\n Oin\n Gloin\n Bifur\n Bofur\n Bombur\n Dwalin\n Balin\n Thorin\n Fili\n Kili', '2024-12-22 15:34:38.509690', '2024-12-22 15:34:38.509690', 'FAILED', 'Vamos todos encontrar a montanha!'),
	(106, 8, '1\n1\n1\n1 0', 'Nao foi dessa vez!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'FAILED', 'Upou de Nivel!'),
	(107, 8, '2\n2 3\n1 2\n10 1', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'PASSED', 'Upou de Nivel!'),
	(108, 8, '3\n1 1 1\n1 1 1\n5 0', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'FAILED', 'Nao foi dessa vez!'),
	(109, 8, '4\n2 2 2 2\n1 1 1 1\n10 1', 'Nao foi dessa vez!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'FAILED', 'Upou de Nivel!'),
	(110, 8, '5\n1 2 3 4 5\n1 1 1 1 1\n20 1', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'PASSED', 'Upou de Nivel!'),
	(111, 8, '3\n5 5 5\n2 2 2\n30 0', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'PASSED', 'Upou de Nivel!'),
	(112, 8, '6\n1 2 3 4 5 6\n1 2 3 4 5 1\n50 2', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'PASSED', 'Upou de Nivel!'),
	(113, 8, '4\n10 10 10 10\n1 1 1 1\n50 0', 'Upou de Nivel!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'FAILED', 'Nao foi dessa vez!'),
	(114, 8, '5\n1 1 1 1 1\n5 5 5 5 5\n50 0', 'Nao foi dessa vez!', '2024-12-22 15:34:50.299234', '2024-12-22 15:34:50.299234', 'PASSED', 'Nao foi dessa vez!'),
	(115, 8, '10\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n20 0', 'Upou de Nivel!', '2024-12-22 15:34:50.306825', '2024-12-22 15:34:50.306825', 'FAILED', 'Nao foi dessa vez!'),
	(116, 8, '10\n10 10 10 10 10 10 10 10 10 10\n5 5 5 5 5 5 5 5 5 5\n500 0', 'Upou de Nivel!', '2024-12-22 15:34:50.306825', '2024-12-22 15:34:50.306825', 'PASSED', 'Upou de Nivel!'),
	(117, 8, '10\n1 2 3 4 5 6 7 8 9 10\n1 1 1 1 1 1 1 1 1 1\n100 0', 'Upou de Nivel!', '2024-12-22 15:34:50.308847', '2024-12-22 15:34:50.308847', 'FAILED', 'Nao foi dessa vez!'),
	(118, 8, '5\n10 10 10 10 10\n5 5 5 5 5\n300 0', 'Upou de Nivel!', '2024-12-22 15:34:50.308847', '2024-12-22 15:34:50.308847', 'FAILED', 'Nao foi dessa vez!'),
	(119, 8, '5\n1 2 3 4 5\n1 2 3 4 5\n50 1', 'Upou de Nivel!', '2024-12-22 15:34:50.308847', '2024-12-22 15:34:50.308847', 'PASSED', 'Upou de Nivel!'),
	(120, 8, '5\n1 1 1 1 1\n1 1 1 1 1\n10 2', 'Nao foi dessa vez!', '2024-12-22 15:34:50.308847', '2024-12-22 15:34:50.308847', 'FAILED', 'Upou de Nivel!'),
	(121, 9, '1\n YODA 1 0\n', 'YODA 1\n', '2024-12-22 15:35:07.886668', '2024-12-22 15:35:07.886668', 'PASSED', 'YODA 1\n'),
	(122, 9, '2\n LUKE 2 1\n LEIA 3 2\n', 'LEIA 1\n LUKE 1\n', '2024-12-22 15:35:07.886668', '2024-12-22 15:35:07.886668', 'FAILED', 'LEIA 1\nLUKE 1\n'),
	(123, 9, '3\n ANAKIN 5 3\n OBIWAN 4 1\n PADME 2 0\n', 'ANAKIN 2\n OBIWAN 3\n PADME 2\n', '2024-12-22 15:35:07.894404', '2024-12-22 15:35:07.894404', 'FAILED', 'ANAKIN 2\nOBIWAN 3\nPADME 2\n'),
	(124, 9, '4\n MACE 3 1\n AHSOKA 2 0\n YODA 5 2\n OBIWAN 4 3\n', 'AHSOKA 2\n MACE 2\n OBIWAN 1\n YODA 3\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'AHSOKA 2\nMACE 2\nOBIWAN 1\nYODA 3\n'),
	(125, 9, '5\n JARJAR 1 1\n HAN 2 0\n CHEWIE 3 1\n LANDO 4 2\n BOBA 5 0\n', 'BOBA 5\n CHEWIE 2\n HAN 2\n LANDO 2\n JARJAR 0\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'BOBA 5\nCHEWIE 2\nHAN 2\nJARJAR 0\nLANDO 2\n'),
	(126, 9, '6\n REY 3 1\n FINN 2 1\n POE 4 0\n ROSE 1 0\n KYLO 5 3\n PHASMA 3 2\n', 'FINN 1\n PHASMA 1\n POE 4\n REY 2\n ROSE 1\n KYLO 2\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'FINN 1\nKYLO 2\nPHASMA 1\nPOE 4\nREY 2\nROSE 1\n'),
	(127, 9, '7\n A 1 0\n B 1 1\n C 1 0\n D 1 0\n E 1 1\n F 1 0\n G 1 0\n', 'A 1\n C 1\n D 1\n F 1\n G 1\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'A 1\nB 0\nC 1\nD 1\nE 0\nF 1\nG 1\n'),
	(128, 9, '8\n H 2 1\n I 3 2\n J 4 1\n K 5 0\n L 6 3\n M 7 4\n N 8 5\n O 9 0\n', 'K 5\n H 1\n I 1\n J 3\n L 3\n M 3\n N 3\n O 9\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'H 1\nI 1\nJ 3\nK 5\nL 3\nM 3\nN 3\nO 9\n'),
	(129, 9, '10\n A 10 5\n B 9 4\n C 8 3\n D 7 2\n E 6 1\n F 5 0\n G 4 0\n H 3 0\n I 2 0\n J 1 0\n', 'A 5\n B 5\n C 5\n D 5\n E 5\n F 5\n G 4\n H 3\n I 2\n J 1\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'A 5\nB 5\nC 5\nD 5\nE 5\nF 5\nG 4\nH 3\nI 2\nJ 1\n'),
	(130, 9, '3\n ZZZZZ 10 5\n YYYYY 10 0\n XXXXX 10 10\n', 'YYYYY 10\n ZZZZZ 5\n XXXXX 0\n', '2024-12-22 15:35:07.896658', '2024-12-22 15:35:07.896658', 'FAILED', 'XXXXX 0\nYYYYY 10\nZZZZZ 5\n'),
	(131, 9, '4\n AAAA 10 0\n BBBB 10 10\n CCCC 10 5\n DDDD 10 2\n', 'AAAA 10\n CCCC 5\n DDDD 8\n BBBB 0\n', '2024-12-22 15:35:07.906632', '2024-12-22 15:35:07.906632', 'FAILED', 'AAAA 10\nBBBB 0\nCCCC 5\nDDDD 8\n'),
	(132, 9, '5\n AAAAA 5 0\n BBBBB 5 5\n CCCCC 5 2\n DDDDD 5 1\n EEEEE 5 3\n', 'AAAAA 5\n CCCCC 3\n DDDDD 4\n EEEEE 2\n BBBBB 0\n', '2024-12-22 15:35:07.906632', '2024-12-22 15:35:07.906632', 'FAILED', 'AAAAA 5\nBBBBB 0\nCCCCC 3\nDDDDD 4\nEEEEE 2\n'),
	(133, 9, '1\n Z 100 50\n', 'Z 50\n', '2024-12-22 15:35:07.910184', '2024-12-22 15:35:07.910184', 'PASSED', 'Z 50\n'),
	(134, 9, '2\n A 100 0\n B 100 100\n', 'A 100\n B 0\n', '2024-12-22 15:35:07.910184', '2024-12-22 15:35:07.910184', 'FAILED', 'A 100\nB 0\n'),
	(135, 9, '3\n A 100 50\n B 100 25\n C 100 75\n', 'A 50\n B 75\n C 25\n', '2024-12-22 15:35:07.910184', '2024-12-22 15:35:07.910184', 'FAILED', 'A 50\nB 75\nC 25\n'),
	(136, 9, '3\n AAA 1 0\n BBB 1 1\n CCC 1 0\n', 'AAA 1\n CCC 1\n BBB 0\n', '2024-12-22 15:35:07.910184', '2024-12-22 15:35:07.910184', 'FAILED', 'AAA 1\nBBB 0\nCCC 1\n'),
	(137, 10, '1 1 2000\n1 1 2001\n1 1 1999\n', '1 1 1999\n1 1 2000\n1 1 2001\n', '2024-12-22 15:35:24.255028', '2024-12-22 15:35:24.255028', 'PASSED', '1 1 1999\n1 1 2000\n1 1 2001\n'),
	(138, 10, '15 5 2020\n15 5 2019\n15 5 2021\n', '15 5 2019\n15 5 2020\n15 5 2021\n', '2024-12-22 15:35:24.257651', '2024-12-22 15:35:24.257651', 'PASSED', '15 5 2019\n15 5 2020\n15 5 2021\n'),
	(139, 10, '31 12 1999\n1 1 2000\n30 12 1999\n', '30 12 1999\n31 12 1999\n1 1 2000\n', '2024-12-22 15:35:24.259722', '2024-12-22 15:35:24.259722', 'PASSED', '30 12 1999\n31 12 1999\n1 1 2000\n'),
	(140, 10, '29 2 2020\n28 2 2020\n1 3 2020\n', '28 2 2020\n29 2 2020\n1 3 2020\n', '2024-12-22 15:35:24.262721', '2024-12-22 15:35:24.262721', 'PASSED', '28 2 2020\n29 2 2020\n1 3 2020\n'),
	(141, 10, '1 1 1900\n1 1 2000\n1 1 1800\n', '1 1 1800\n1 1 1900\n1 1 2000\n', '2024-12-22 15:35:24.264725', '2024-12-22 15:35:24.264725', 'PASSED', '1 1 1800\n1 1 1900\n1 1 2000\n'),
	(142, 10, '5 5 2022\n5 5 2021\n5 5 2020\n5 5 2019\n', '5 5 2019\n5 5 2020\n5 5 2021\n5 5 2022\n', '2024-12-22 15:35:24.267278', '2024-12-22 15:35:24.267278', 'PASSED', '5 5 2019\n5 5 2020\n5 5 2021\n5 5 2022\n'),
	(143, 10, '1 1 2023\n1 1 2022\n1 1 2021\n1 1 2020\n1 1 2019\n', '1 1 2019\n1 1 2020\n1 1 2021\n1 1 2022\n1 1 2023\n', '2024-12-22 15:35:24.268361', '2024-12-22 15:35:24.268361', 'PASSED', '1 1 2019\n1 1 2020\n1 1 2021\n1 1 2022\n1 1 2023\n'),
	(144, 10, '15 8 1945\n15 8 1946\n15 8 1944\n', '15 8 1944\n15 8 1945\n15 8 1946\n', '2024-12-22 15:35:24.270358', '2024-12-22 15:35:24.270358', 'PASSED', '15 8 1944\n15 8 1945\n15 8 1946\n'),
	(145, 10, '1 1 2022\n1 1 2022\n1 1 2022\n', '1 1 2022\n1 1 2022\n1 1 2022\n', '2024-12-22 15:35:24.271307', '2024-12-22 15:35:24.271307', 'PASSED', '1 1 2022\n1 1 2022\n1 1 2022\n'),
	(146, 10, '31 12 2021\n1 1 2022\n30 12 2021\n29 12 2021\n', '29 12 2021\n30 12 2021\n31 12 2021\n1 1 2022\n', '2024-12-22 15:35:24.273346', '2024-12-22 15:35:24.273346', 'PASSED', '29 12 2021\n30 12 2021\n31 12 2021\n1 1 2022\n'),
	(147, 10, '1 1 2000\n1 1 2000\n1 1 2000\n1 1 2000\n', '1 1 2000\n1 1 2000\n1 1 2000\n1 1 2000\n', '2024-12-22 15:35:24.274346', '2024-12-22 15:35:24.274346', 'PASSED', '1 1 2000\n1 1 2000\n1 1 2000\n1 1 2000\n'),
	(148, 10, '1 1 2020\n2 2 2020\n3 3 2020\n4 4 2020\n5 5 2020\n6 6 2020\n7 7 2020\n8 8 2020\n9 9 2020\n10 10 2020\n', '1 1 2020\n2 2 2020\n3 3 2020\n4 4 2020\n5 5 2020\n6 6 2020\n7 7 2020\n8 8 2020\n9 9 2020\n10 10 2020\n', '2024-12-22 15:35:24.275311', '2024-12-22 15:35:24.275311', 'PASSED', '1 1 2020\n2 2 2020\n3 3 2020\n4 4 2020\n5 5 2020\n6 6 2020\n7 7 2020\n8 8 2020\n9 9 2020\n10 10 2020\n'),
	(149, 10, '1 1 2023\n1 1 2022\n1 1 2021\n1 1 2020\n1 1 2019\n1 1 2018\n1 1 2017\n1 1 2016\n1 1 2015\n1 1 2014\n', '1 1 2014\n1 1 2015\n1 1 2016\n1 1 2017\n1 1 2018\n1 1 2019\n1 1 2020\n1 1 2021\n1 1 2022\n1 1 2023\n', '2024-12-22 15:35:24.277070', '2024-12-22 15:35:24.277070', 'PASSED', '1 1 2014\n1 1 2015\n1 1 2016\n1 1 2017\n1 1 2018\n1 1 2019\n1 1 2020\n1 1 2021\n1 1 2022\n1 1 2023\n');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
