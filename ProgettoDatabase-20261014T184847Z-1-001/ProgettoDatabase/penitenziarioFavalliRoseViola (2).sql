-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Dic 15, 2025 alle 08:54
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `penitenziario`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `carcerato`
--

CREATE TABLE `carcerato` (
  `id_carc` int(11) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `data_nascita` date NOT NULL,
  `nazionalita` enum('Italiana','Rumena','Albanese','Marocchina','Senegalese','Nigeriana','Cinese','Indiana','Giapponese','Statunitense','Brasiliana','Messicana') NOT NULL,
  `pena` text NOT NULL,
  `reato` text NOT NULL,
  `locType` enum('Cella','Cortile','Mensa') DEFAULT 'Cella',
  `locId` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `carcerato`
--

INSERT INTO `carcerato` (`id_carc`, `cf`, `nome`, `cognome`, `data_nascita`, `nazionalita`, `pena`, `reato`, `locType`, `locId`) VALUES
(1, 'ITL001', 'Mario', 'Rossi', '1985-01-01', 'Italiana', '5 anni', 'Furto', 'Cella', 'A12'),
(2, 'ITL002', 'Giulia', 'Bianchi', '1990-02-02', 'Italiana', '3 anni', 'Truffa', 'Cella', 'A13'),
(3, 'ITL003', 'Luca', 'Verdi', '1988-03-03', 'Italiana', '7 anni', 'Rapina', 'Cella', 'A14'),
(4, 'RUM001', 'Andrei', 'Popescu', '1987-04-04', 'Rumena', '4 anni', 'Furto', 'Cella', 'B04'),
(5, 'RUM002', 'Elena', 'Ionescu', '1992-05-05', 'Rumena', '6 anni', 'Truffa', 'Cella', 'C10'),
(6, 'RUM003', 'Mihai', 'Georgescu', '1989-06-06', 'Rumena', '8 anni', 'Rapina', 'Cella', 'C10'),
(7, 'ALB001', 'Arben', 'Duka', '1991-07-07', 'Albanese', '5 anni', 'Furto', 'Cella', 'C10'),
(8, 'ALB002', 'Fatmir', 'Hoxha', '1993-08-08', 'Albanese', '9 anni', 'Truffa', 'Cella', 'C10'),
(9, 'ALB003', 'Gentian', 'Demiri', '1995-09-09', 'Albanese', '10 anni', 'Rapina', 'Cella', 'C10'),
(10, 'MAR001', 'Youssef', 'Idrissi', '1986-10-10', 'Marocchina', '6 anni', 'Furto', 'Cella', 'C10'),
(11, 'MAR002', 'Hamid', 'El Fassi', '1994-11-11', 'Marocchina', '7 anni', 'Truffa', 'Cella', 'D01'),
(12, 'MAR003', 'Driss', 'Bahri', '1997-12-12', 'Marocchina', '8 anni', 'Rapina', 'Cella', 'D02'),
(13, 'SEN001', 'Moussa', 'Diallo', '1988-01-13', 'Senegalese', '4 anni', 'Furto', 'Cella', 'D03'),
(14, 'SEN002', 'Ousmane', 'Ndoye', '1990-02-14', 'Senegalese', '6 anni', 'Truffa', 'Cella', 'D04'),
(15, 'SEN003', 'Baba', 'Traore', '1992-03-15', 'Senegalese', '9 anni', 'Rapina', 'Cella', 'B06'),
(16, 'NIG001', 'Chinua', 'Okokoro', '1985-04-16', 'Nigeriana', '5 anni', 'Furto', 'Cella', 'B07'),
(17, 'NIG002', 'Chidi', 'Nnadi', '1989-05-17', 'Nigeriana', '7 anni', 'Truffa', 'Cella', 'B07'),
(18, 'NIG003', 'Nnamdi', 'Eze', '1993-06-18', 'Nigeriana', '10 anni', 'Rapina', 'Cella', 'B06'),
(19, 'CIN001', 'Li', 'Wei', '1987-07-19', 'Cinese', '6 anni', 'Furto', 'Cella', 'C07'),
(20, 'CIN002', 'Zhang', 'Hua', '1991-08-20', 'Cinese', '8 anni', 'Truffa', 'Cella', 'C07'),
(21, 'CIN003', 'Chen', 'Bo', '1995-09-21', 'Cinese', '9 anni', 'Rapina', 'Cella', 'C07'),
(22, 'IND001', 'Raj', 'Kumar', '1986-10-22', 'Indiana', '5 anni', 'Furto', 'Cella', 'C07'),
(23, 'IND002', 'Priya', 'Singh', '1990-11-23', 'Indiana', '7 anni', 'Truffa', 'Cella', 'C07'),
(24, 'IND003', 'Amit', 'Patel', '1994-12-24', 'Indiana', '10 anni', 'Rapina', 'Cella', 'C07'),
(25, 'JPN001', 'Kenji', 'Tanaka', '1988-01-25', 'Giapponese', '4 anni', 'Furto', 'Cella', 'C08'),
(26, 'JPN002', 'Yuki', 'Sato', '1992-02-26', 'Giapponese', '6 anni', 'Truffa', 'Cella', 'C08'),
(27, 'JPN003', 'Hiroshi', 'Kobayashi', '1996-03-27', 'Giapponese', '9 anni', 'Rapina', 'Cella', 'C08'),
(28, 'USA001', 'John', 'Smith', '1985-04-28', 'Statunitense', '5 anni', 'Furto', 'Cella', 'C08'),
(29, 'USA002', 'Emily', 'Johnson', '1989-05-29', 'Statunitense', '7 anni', 'Truffa', 'Cella', 'C08'),
(30, 'USA003', 'Michael', 'Brown', '1993-06-30', 'Statunitense', '10 anni', 'Rapina', 'Cella', 'C08'),
(31, 'BRA001', 'Carlos', 'Silva', '1987-07-01', 'Brasiliana', '6 anni', 'Furto', 'Cella', 'C09'),
(32, 'BRA002', 'Ana', 'Souza', '1991-08-02', 'Brasiliana', '8 anni', 'Truffa', 'Cella', 'C09'),
(33, 'BRA003', 'Pedro', 'Oliveira', '1995-09-03', 'Brasiliana', '9 anni', 'Rapina', 'Cella', 'C09'),
(34, 'MEX001', 'Luis', 'Hernandez', '1986-10-04', 'Messicana', '5 anni', 'Furto', 'Cella', 'C09'),
(35, 'MEX002', 'Maria', 'Lopez', '1990-11-05', 'Messicana', '7 anni', 'Truffa', 'Cella', 'C09'),
(36, 'MEX003', 'Jose', 'Garcia', '1994-12-06', 'Messicana', '10 anni', 'Rapina', 'Cella', 'C09'),
(37, 'ITL004', 'Paolo', 'Ferrari', '1986-01-01', 'Italiana', '4 anni', 'Furto', 'Cella', 'A12'),
(38, 'ITL005', 'Chiara', 'Romano', '1991-02-02', 'Italiana', '6 anni', 'Truffa', 'Cella', 'A12'),
(39, 'ITL006', 'Stefano', 'Greco', '1989-03-03', 'Italiana', '8 anni', 'Rapina', 'Cella', 'A12'),
(40, 'RUM004', 'Ion', 'Popa', '1988-04-04', 'Rumena', '5 anni', 'Furto', 'Cella', 'A13'),
(41, 'RUM005', 'Alina', 'Petrescu', '1993-05-05', 'Rumena', '7 anni', 'Truffa', 'Cella', 'A13'),
(42, 'RUM006', 'Vasile', 'Marin', '1990-06-06', 'Rumena', '9 anni', 'Rapina', 'Cella', 'A13'),
(43, 'ALB004', 'Besnik', 'Kola', '1992-07-07', 'Albanese', '6 anni', 'Furto', 'Cella', 'A14'),
(44, 'ALB005', 'Shqipe', 'Leka', '1994-08-08', 'Albanese', '8 anni', 'Truffa', 'Cella', 'A14'),
(45, 'ALB006', 'Dritan', 'Meta', '1996-09-09', 'Albanese', '10 anni', 'Rapina', 'Cella', 'A14'),
(46, 'MAR004', 'Karim', 'Zouhair', '1987-10-10', 'Marocchina', '5 anni', 'Furto', 'Cella', 'B04'),
(47, 'MAR005', 'Samira', 'Benali', '1992-11-11', 'Marocchina', '7 anni', 'Truffa', 'Cella', 'B05'),
(48, 'MAR006', 'Omar', 'El Idrissi', '1995-12-12', 'Marocchina', '9 anni', 'Rapina', 'Cella', 'B05'),
(49, 'SEN004', 'Abdou', 'Fall', '1989-01-13', 'Senegalese', '4 anni', 'Furto', 'Cella', 'B06'),
(50, 'SEN005', 'Awa', 'Diop', '1991-02-14', 'Senegalese', '6 anni', 'Truffa', 'Cella', 'B06'),
(51, 'SEN006', 'Cheikh', 'Sarr', '1993-03-15', 'Senegalese', '9 anni', 'Rapina', 'Cella', 'B07'),
(52, 'NIG004', 'Obi', 'Okeke', '1986-04-16', 'Nigeriana', '5 anni', 'Furto', 'Cella', 'B07'),
(53, 'NIG005', 'Ngozi', 'Eze', '1990-05-17', 'Nigeriana', '7 anni', 'Truffa', 'Cella', 'B07'),
(54, 'NIG006', 'Ifeanyi', 'Nwosu', '1994-06-18', 'Nigeriana', '10 anni', 'Rapina', 'Cella', 'B07'),
(55, 'ENEMEL2007', 'Enea', 'Melloni', '2007-01-11', 'Italiana', 'x', 'x', 'Cella', 'A15');

-- --------------------------------------------------------

--
-- Struttura della tabella `carcerato_cortile`
--

CREATE TABLE `carcerato_cortile` (
  `id_carc` int(11) NOT NULL,
  `id_cortile` int(11) NOT NULL,
  `orario` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `carcerato_mensa`
--

CREATE TABLE `carcerato_mensa` (
  `id_carc` int(11) NOT NULL,
  `id_mensa` int(11) NOT NULL,
  `orario` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `cella`
--

CREATE TABLE `cella` (
  `id_cella` varchar(4) NOT NULL,
  `sicurezza` enum('Bassa','Media','Alta','Isolamento') NOT NULL,
  `capienza` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `cella`
--

INSERT INTO `cella` (`id_cella`, `sicurezza`, `capienza`) VALUES
('A12', 'Media', 4),
('A13', 'Media', 4),
('A14', 'Media', 4),
('A15', 'Media', 4),
('B04', 'Alta', 2),
('B05', 'Alta', 2),
('B06', 'Alta', 2),
('B07', 'Alta', 2),
('C07', 'Bassa', 6),
('C08', 'Bassa', 6),
('C09', 'Bassa', 6),
('C10', 'Bassa', 6),
('D01', 'Isolamento', 1),
('D02', 'Isolamento', 1),
('D03', 'Isolamento', 1),
('D04', 'Isolamento', 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `cortile`
--

CREATE TABLE `cortile` (
  `id_cortile` int(11) NOT NULL,
  `area` enum('Palestra','Basket','Calcio') NOT NULL,
  `capienza` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `cortile`
--

INSERT INTO `cortile` (`id_cortile`, `area`, `capienza`) VALUES
(1, 'Palestra', 20),
(2, 'Basket', 15),
(3, 'Calcio', 30);

-- --------------------------------------------------------

--
-- Struttura della tabella `mensa`
--

CREATE TABLE `mensa` (
  `id_mensa` int(11) NOT NULL,
  `menu` text NOT NULL,
  `capienza` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `mensa`
--

INSERT INTO `mensa` (`id_mensa`, `menu`, `capienza`) VALUES
(1, 'Pasta, pollo, verdure', 40),
(2, 'Riso, manzo, frutta', 35);

-- --------------------------------------------------------

--
-- Struttura della tabella `personale`
--

CREATE TABLE `personale` (
  `id_pers` int(11) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `data_nascita` date NOT NULL,
  `ruolo` enum('Direttore','Secondino','Guardia','Cuoco','Medico','Educatore','Psicologo','Amministrativo') NOT NULL,
  `dotazione` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `personale`
--

INSERT INTO `personale` (`id_pers`, `cf`, `nome`, `cognome`, `data_nascita`, `ruolo`, `dotazione`) VALUES
(1, 'FVLVNI80A01H501A', 'Ivan', 'Favalli', '1980-01-01', 'Direttore', 3),
(2, 'VLIVNI90B10H501B', 'Ivan', 'Viola', '1990-02-10', 'Secondino', 2),
(3, 'DNLRSE85C20H501C', 'Rose', 'Daniele', '1985-03-20', 'Cuoco', 1),
(4, 'PLLNDR75D15H501D', 'Andrea', 'Pelle', '1975-04-15', 'Guardia', 2),
(5, 'CNTMRA88E22H501E', 'Maria', 'Conti', '1988-05-22', 'Medico', 1),
(6, 'RSCMNL70F30H501F', 'Manuel', 'Russo', '1970-06-30', 'Educatore', 0),
(10, 'BNCFRZ87L05H501L', 'Franco', 'Bianchi', '1987-10-05', 'Guardia', 2),
(11, 'MARMAI1982P', 'Mara', 'Maionchi', '1982-12-12', 'Medico', 1),
(12, 'GIABEL1982P', 'Gianna', 'Bello', '1982-12-12', 'Psicologo', 4),
(13, 'ROBMIN1982P', 'Roberta', 'Minelli', '1982-12-12', 'Amministrativo', 12),
(14, 'PIPBAU1992P', 'Pippo', 'Baudo', '1992-12-12', 'Medico', 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `turno`
--

CREATE TABLE `turno` (
  `id_turno` int(11) NOT NULL,
  `id_pers` int(11) DEFAULT NULL,
  `inizio` datetime NOT NULL,
  `fine` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `turno`
--

INSERT INTO `turno` (`id_turno`, `id_pers`, `inizio`, `fine`) VALUES
(40, 2, '2025-12-04 19:17:00', '2025-12-04 19:18:00'),
(48, 4, '2025-12-15 08:53:00', '2025-12-15 08:54:00');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `carcerato`
--
ALTER TABLE `carcerato`
  ADD PRIMARY KEY (`id_carc`),
  ADD UNIQUE KEY `cf` (`cf`);

--
-- Indici per le tabelle `carcerato_cortile`
--
ALTER TABLE `carcerato_cortile`
  ADD PRIMARY KEY (`id_carc`,`id_cortile`),
  ADD KEY `id_cortile` (`id_cortile`);

--
-- Indici per le tabelle `carcerato_mensa`
--
ALTER TABLE `carcerato_mensa`
  ADD PRIMARY KEY (`id_carc`,`id_mensa`),
  ADD KEY `id_mensa` (`id_mensa`);

--
-- Indici per le tabelle `cella`
--
ALTER TABLE `cella`
  ADD PRIMARY KEY (`id_cella`);

--
-- Indici per le tabelle `cortile`
--
ALTER TABLE `cortile`
  ADD PRIMARY KEY (`id_cortile`);

--
-- Indici per le tabelle `mensa`
--
ALTER TABLE `mensa`
  ADD PRIMARY KEY (`id_mensa`);

--
-- Indici per le tabelle `personale`
--
ALTER TABLE `personale`
  ADD PRIMARY KEY (`id_pers`),
  ADD UNIQUE KEY `cf` (`cf`);

--
-- Indici per le tabelle `turno`
--
ALTER TABLE `turno`
  ADD PRIMARY KEY (`id_turno`),
  ADD KEY `id_pers` (`id_pers`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `carcerato`
--
ALTER TABLE `carcerato`
  MODIFY `id_carc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT per la tabella `cortile`
--
ALTER TABLE `cortile`
  MODIFY `id_cortile` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT per la tabella `mensa`
--
ALTER TABLE `mensa`
  MODIFY `id_mensa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `personale`
--
ALTER TABLE `personale`
  MODIFY `id_pers` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `turno`
--
ALTER TABLE `turno`
  MODIFY `id_turno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `carcerato_cortile`
--
ALTER TABLE `carcerato_cortile`
  ADD CONSTRAINT `carcerato_cortile_ibfk_1` FOREIGN KEY (`id_carc`) REFERENCES `carcerato` (`id_carc`),
  ADD CONSTRAINT `carcerato_cortile_ibfk_2` FOREIGN KEY (`id_cortile`) REFERENCES `cortile` (`id_cortile`);

--
-- Limiti per la tabella `carcerato_mensa`
--
ALTER TABLE `carcerato_mensa`
  ADD CONSTRAINT `carcerato_mensa_ibfk_1` FOREIGN KEY (`id_carc`) REFERENCES `carcerato` (`id_carc`),
  ADD CONSTRAINT `carcerato_mensa_ibfk_2` FOREIGN KEY (`id_mensa`) REFERENCES `mensa` (`id_mensa`);

--
-- Limiti per la tabella `turno`
--
ALTER TABLE `turno`
  ADD CONSTRAINT `turno_ibfk_1` FOREIGN KEY (`id_pers`) REFERENCES `personale` (`id_pers`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
