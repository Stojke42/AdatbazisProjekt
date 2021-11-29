-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 28, 2021 at 11:28 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `famtree`
--

-- --------------------------------------------------------

--
-- Table structure for table `EVENTTABLE`
--

CREATE TABLE `EVENTTABLE` (
  `eventid` bigint(100) NOT NULL,
  `personid` bigint(100) NOT NULL,
  `eventdate` date NOT NULL DEFAULT current_timestamp(),
  `eventname` varchar(100) COLLATE utf8mb4_hungarian_ci DEFAULT 'Birth day'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- Dumping data for table `EVENTTABLE`
--

INSERT INTO `EVENTTABLE` (`eventid`, `personid`, `eventdate`, `eventname`) VALUES
(1, 2601997820224, '2022-01-26', 'Birth day'),
(2, 10000019721211, '2021-12-11', 'Birth day'),
(3, 2601997820224, '2023-01-26', 'Birth day'),
(4, 10000019781024, '2023-07-01', 'Wedding anniversary'),
(5, 10000019781024, '2025-07-01', 'Wedding anniversary\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `Mariage`
--

CREATE TABLE `Mariage` (
  `MariageID` bigint(100) NOT NULL,
  `Person1` bigint(100) NOT NULL,
  `Person2` bigint(100) NOT NULL,
  `MariageDate` date NOT NULL,
  `stillgoingon` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- Dumping data for table `Mariage`
--

INSERT INTO `Mariage` (`MariageID`, `Person1`, `Person2`, `MariageDate`, `stillgoingon`) VALUES
(1, 10000019721211, 11000019721212, '1996-07-12', 1),
(2, 10000019450629, 11000019450629, '1971-11-05', 0),
(3, 10000019781024, 11000019781024, '2005-07-01', 1),
(4, 10000019200101, 11000019200101, '1922-11-01', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Person`
--

CREATE TABLE `Person` (
  `personid` bigint(100) NOT NULL DEFAULT 0,
  `fatherid` bigint(100) DEFAULT 0,
  `motherid` bigint(100) DEFAULT 0,
  `name` varchar(100) COLLATE utf8mb4_hungarian_ci DEFAULT 'SOMEONE',
  `dateofbirth` date DEFAULT current_timestamp(),
  `dateofdeth` date DEFAULT NULL,
  `gender` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- Dumping data for table `Person`
--

INSERT INTO `Person` (`personid`, `fatherid`, `motherid`, `name`, `dateofbirth`, `dateofdeth`, `gender`) VALUES
(2601997820224, 10000019721211, 11000019721212, 'Stoisavljevic Aleksandar', '1997-01-26', NULL, 1),
(10000019200101, NULL, NULL, 'Stoisavljevic Jovo', '1920-01-01', '2021-11-01', 1),
(10000019200601, NULL, NULL, 'Berta Sandor', '1920-06-01', NULL, 1),
(10000019400101, NULL, NULL, 'Petrovic Stipan', '1940-01-01', NULL, 1),
(10000019450629, NULL, NULL, 'Sinka Peter', '1945-06-29', NULL, 1),
(10000019451127, 10000019200101, 11000019200101, 'Stoisavljevic Ljubisav', '1945-11-27', NULL, 1),
(10000019500101, NULL, NULL, 'Vago Tibor', '1950-01-01', NULL, 1),
(10000019721211, 10000019451127, 11000019451127, 'Stoisavljevic Dragan', '1972-12-11', NULL, 1),
(10000019781024, 10000019451127, 11000019451127, 'Stoisavljevic Aleksandar', '1978-10-24', NULL, 1),
(10000020010219, 10000019721211, 11000019721212, 'Stoisavljevic Marko', '2001-02-19', NULL, 1),
(10000020100628, 10000019781024, 11000019781024, 'Stoisavljevic Dimitrije', '2010-06-28', NULL, 1),
(11000019200101, NULL, NULL, 'Stoisavljevic Zorka', '1920-01-01', NULL, 0),
(11000019200601, NULL, NULL, 'Berta Julian', '1920-06-01', NULL, 0),
(11000019400101, NULL, NULL, 'Petrovic Jasminka', '1940-01-01', NULL, 0),
(11000019450629, NULL, NULL, 'Sinka Panna', '1945-06-29', NULL, 0),
(11000019451127, 10000019200601, 11000019200601, 'Berta Matild', '1945-11-27', NULL, 0),
(11000019500101, 10000019450629, 11000019450629, 'Sinka Zsuzsanna', '1950-01-01', NULL, 0),
(11000019721212, 10000019450629, 11000019450629, 'Sinka Anna', '1972-12-12', NULL, 0),
(11000019781024, 10000019400101, 11000019400101, 'Petrovic Ivana', '1978-10-24', NULL, 0),
(11000019850101, 11000019500101, 10000019500101, 'Vago Orsolya', '1985-01-01', NULL, 0),
(11000019850102, 10000019500101, 11000019500101, 'Vago Edina', '1985-01-02', NULL, 0),
(11000020140704, 10000019781024, 11000019781024, 'Stoisavljevic Danica', '2014-07-04', NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `Relationship`
--

CREATE TABLE `Relationship` (
  `RelationshipID` bigint(100) NOT NULL,
  `Person1` bigint(100) NOT NULL,
  `Person2` bigint(100) NOT NULL,
  `RelationshipName` varchar(100) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- Dumping data for table `Relationship`
--

INSERT INTO `Relationship` (`RelationshipID`, `Person1`, `Person2`, `RelationshipName`) VALUES
(2, 2601997820224, 10000020010219, 'Brothers'),
(3, 10000020100628, 11000020140704, 'Sister'),
(4, 11000019721212, 2601997820224, 'Son'),
(5, 11000019721212, 10000020010219, 'Son'),
(6, 11000019781024, 10000020100628, 'Son'),
(7, 11000019781024, 11000020140704, 'Dougther'),
(8, 11000019400101, 11000019781024, 'Dougther'),
(9, 11000019450629, 11000019721212, 'Dougther'),
(10, 11000019200601, 11000019451127, 'Dougther'),
(11, 10000019200601, 11000019451127, 'Dougther'),
(12, 11000019451127, 10000019721211, 'Son'),
(13, 10000019721211, 2601997820224, 'Son'),
(14, 10000019721211, 2601997820224, 'Son'),
(15, 2601997820224, 11000019850101, 'Cousin'),
(16, 2601997820224, 11000019850102, 'Cousin'),
(17, 2601997820224, 11000019500101, 'Aunt'),
(18, 2601997820224, 10000019781024, 'Uncle');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(50) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `firstname` varchar(100) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `firstname`, `password`) VALUES
('aleksandarfax@gmail.com', 'Aleksandar', 'sha256$eeECWJoDS2E0i4oK$77cd6ec3d36b224edcfbf9e1d5f94a839b6abcdfb8820bf90d2c736cbc442dd4'),
('aleksandarstoisavljevic@gmail.com', 'Aleksandar', 'sha256$0vrTs42imnWnZIci$9b5349914f33ea7443e05ee9fad19f0b0fe8a7d58a7aa8e9a8a61c4b8d1b8a7e'),
('bestofbalkan16@gmail.com', 'Ana', 'sha256$Y6vScYwrg4v8d2hG$3aecb419fb48c2c60f3e694d41e0b02cc5e5c6dd689bd580be78a0f5d64fc036');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `EVENTTABLE`
--
ALTER TABLE `EVENTTABLE`
  ADD PRIMARY KEY (`eventid`),
  ADD KEY `personid` (`personid`);

--
-- Indexes for table `Mariage`
--
ALTER TABLE `Mariage`
  ADD PRIMARY KEY (`MariageID`),
  ADD KEY `Person1` (`Person1`),
  ADD KEY `Person2` (`Person2`);

--
-- Indexes for table `Person`
--
ALTER TABLE `Person`
  ADD PRIMARY KEY (`personid`),
  ADD KEY `fatherid` (`fatherid`),
  ADD KEY `motherid` (`motherid`);

--
-- Indexes for table `Relationship`
--
ALTER TABLE `Relationship`
  ADD PRIMARY KEY (`RelationshipID`),
  ADD KEY `Person1` (`Person1`),
  ADD KEY `Person2` (`Person2`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `EVENTTABLE`
--
ALTER TABLE `EVENTTABLE`
  MODIFY `eventid` bigint(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Mariage`
--
ALTER TABLE `Mariage`
  MODIFY `MariageID` bigint(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Relationship`
--
ALTER TABLE `Relationship`
  MODIFY `RelationshipID` bigint(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `EVENTTABLE`
--
ALTER TABLE `EVENTTABLE`
  ADD CONSTRAINT `EVENTTABLE_ibfk_1` FOREIGN KEY (`personid`) REFERENCES `Person` (`personid`);

--
-- Constraints for table `Mariage`
--
ALTER TABLE `Mariage`
  ADD CONSTRAINT `Mariage_ibfk_1` FOREIGN KEY (`Person1`) REFERENCES `Person` (`personid`),
  ADD CONSTRAINT `Mariage_ibfk_2` FOREIGN KEY (`Person2`) REFERENCES `Person` (`personid`);

--
-- Constraints for table `Person`
--
ALTER TABLE `Person`
  ADD CONSTRAINT `Person_ibfk_1` FOREIGN KEY (`fatherid`) REFERENCES `Person` (`personid`),
  ADD CONSTRAINT `Person_ibfk_2` FOREIGN KEY (`motherid`) REFERENCES `Person` (`personid`);

--
-- Constraints for table `Relationship`
--
ALTER TABLE `Relationship`
  ADD CONSTRAINT `Relationship_ibfk_1` FOREIGN KEY (`Person1`) REFERENCES `Person` (`personid`),
  ADD CONSTRAINT `Relationship_ibfk_2` FOREIGN KEY (`Person2`) REFERENCES `Person` (`personid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
