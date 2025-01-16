-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 16 jan. 2025 à 14:37
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Bibliotheque`
--

-- --------------------------------------------------------

--
-- Structure de la table `Administrateur`
--

CREATE TABLE `Administrateur` (
  `ID_Admin` int(11) NOT NULL,
  `Est_admin` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Administrateur`
--

INSERT INTO `Administrateur` (`ID_Admin`, `Est_admin`) VALUES
(1, 1),
(4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `Auteur`
--

CREATE TABLE `Auteur` (
  `ID_Auteur` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `Prenom` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Auteur`
--

INSERT INTO `Auteur` (`ID_Auteur`, `Nom`, `Prenom`) VALUES
(1, 'Asimov', 'Isaac'),
(2, 'Tolkien', 'J.R.R.'),
(3, 'Sapiens', 'Yuval Noah'),
(4, 'Rowling', 'J.K.');

-- --------------------------------------------------------

--
-- Structure de la table `Collection`
--

CREATE TABLE `Collection` (
  `ID_Collection` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Collection`
--

INSERT INTO `Collection` (`ID_Collection`, `Nom`) VALUES
(1, 'Science Fiction'),
(2, 'Fantasy'),
(3, 'History'),
(4, 'Biography');

-- --------------------------------------------------------

--
-- Structure de la table `Emprunt`
--

CREATE TABLE `Emprunt` (
  `ID_Emprunt` int(11) NOT NULL,
  `Date_de_retour` date DEFAULT NULL,
  `Date_d_emprunt` date NOT NULL,
  `ID_Livre` int(11) DEFAULT NULL,
  `ID_Utilisateur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Emprunt`
--

INSERT INTO `Emprunt` (`ID_Emprunt`, `Date_de_retour`, `Date_d_emprunt`, `ID_Livre`, `ID_Utilisateur`) VALUES
(1, '2024-01-10', '2024-01-01', 1, 1),
(2, '2024-01-15', '2024-01-05', 2, 2);

-- --------------------------------------------------------

--
-- Structure de la table `Genre`
--

CREATE TABLE `Genre` (
  `ID_Genre` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Genre`
--

INSERT INTO `Genre` (`ID_Genre`, `Nom`) VALUES
(1, 'Novel'),
(2, 'Educational'),
(3, 'Adventure'),
(4, 'Historical');

-- --------------------------------------------------------

--
-- Structure de la table `Livre`
--

CREATE TABLE `Livre` (
  `ID_Livre` int(11) NOT NULL,
  `Titre` varchar(255) NOT NULL,
  `Date_de_publication` date DEFAULT NULL,
  `ISBN` varchar(20) DEFAULT NULL,
  `Synopsis` text DEFAULT NULL,
  `ID_Collection` int(11) DEFAULT NULL,
  `ID_Auteur` int(11) DEFAULT NULL,
  `ID_Genre` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Livre`
--

INSERT INTO `Livre` (`ID_Livre`, `Titre`, `Date_de_publication`, `ISBN`, `Synopsis`, `ID_Collection`, `ID_Auteur`, `ID_Genre`) VALUES
(1, 'Foundation', '1951-06-01', '978-0-123456-01', 'Epic science fiction story.', 1, 1, 1),
(2, 'The Hobbit', '1937-09-21', '978-0-123456-02', 'Fantasy adventure tale.', 2, 2, 3),
(3, 'Sapiens: A Brief History of Humankind', '2011-09-04', '978-0-123456-03', 'Exploring human history.', 3, 3, 2),
(4, 'Harry Potter and the Sorcerer\'s Stone', '1997-06-26', '978-0-123456-04', 'Magical adventure of Harry Potter.', 2, 4, 3);

-- --------------------------------------------------------

--
-- Structure de la table `Reservation`
--

CREATE TABLE `Reservation` (
  `ID_Reservation` int(11) NOT NULL,
  `Date_de_réservation` date NOT NULL,
  `Statut_reservation` varchar(50) DEFAULT NULL,
  `ID_Livre` int(11) DEFAULT NULL,
  `ID_Utilisateur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Reservation`
--

INSERT INTO `Reservation` (`ID_Reservation`, `Date_de_réservation`, `Statut_reservation`, `ID_Livre`, `ID_Utilisateur`) VALUES
(1, '2024-01-02', 'Pending', 3, 3),
(2, '2024-01-04', 'Confirmed', 4, 2);

-- --------------------------------------------------------

--
-- Structure de la table `Utilisateur`
--

CREATE TABLE `Utilisateur` (
  `ID_Utilisateur` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `Prenom` varchar(100) DEFAULT NULL,
  `Nom_utilisateur` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Mot_de_passe_hash` varchar(255) NOT NULL,
  `Est_actif` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Utilisateur`
--

INSERT INTO `Utilisateur` (`ID_Utilisateur`, `Nom`, `Prenom`, `Nom_utilisateur`, `Email`, `Mot_de_passe_hash`, `Est_actif`) VALUES
(1, 'Doe', 'John', 'johndoe', 'john@example.com', '$2b$12$dM7ldZqD28EgoYr11kHSQ.QqaT6Q5710bS3rYEbl8bA8/GBDpdEsG', 1),
(2, 'Smith', 'Jane', 'janesmith', 'jane@example.com', '$2b$12$N9on68nCdj5F1KrPDEUR1e3t03lNIAqdfRQdtUxuW4zfZgyoH3RHK', 1),
(3, 'Brown', 'Charlie', 'charlieb', 'charlie@example.com', '$2b$12$2sEc.lW2NK2cqbfKf0kSiugBPJU0A0dpKIx/44/5bT1FDG.p6wTH6', 1),
(4, 'Minardi', 'Timeo', 'timeomin', 'timeo.machin@machin.com', '$2b$12$OE7TxxD5WggRcHdtOFwcnuDmtLkghRO9vx.8FSlvHt7HIHu1A34Re', 1);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Administrateur`
--
ALTER TABLE `Administrateur`
  ADD PRIMARY KEY (`ID_Admin`);

--
-- Index pour la table `Auteur`
--
ALTER TABLE `Auteur`
  ADD PRIMARY KEY (`ID_Auteur`);

--
-- Index pour la table `Collection`
--
ALTER TABLE `Collection`
  ADD PRIMARY KEY (`ID_Collection`);

--
-- Index pour la table `Emprunt`
--
ALTER TABLE `Emprunt`
  ADD PRIMARY KEY (`ID_Emprunt`),
  ADD KEY `ID_Livre` (`ID_Livre`),
  ADD KEY `ID_Utilisateur` (`ID_Utilisateur`);

--
-- Index pour la table `Genre`
--
ALTER TABLE `Genre`
  ADD PRIMARY KEY (`ID_Genre`);

--
-- Index pour la table `Livre`
--
ALTER TABLE `Livre`
  ADD PRIMARY KEY (`ID_Livre`),
  ADD UNIQUE KEY `ISBN` (`ISBN`),
  ADD KEY `ID_Collection` (`ID_Collection`),
  ADD KEY `ID_Auteur` (`ID_Auteur`),
  ADD KEY `ID_Genre` (`ID_Genre`);

--
-- Index pour la table `Reservation`
--
ALTER TABLE `Reservation`
  ADD PRIMARY KEY (`ID_Reservation`),
  ADD KEY `ID_Livre` (`ID_Livre`),
  ADD KEY `ID_Utilisateur` (`ID_Utilisateur`);

--
-- Index pour la table `Utilisateur`
--
ALTER TABLE `Utilisateur`
  ADD PRIMARY KEY (`ID_Utilisateur`),
  ADD UNIQUE KEY `Nom_utilisateur` (`Nom_utilisateur`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Auteur`
--
ALTER TABLE `Auteur`
  MODIFY `ID_Auteur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Collection`
--
ALTER TABLE `Collection`
  MODIFY `ID_Collection` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Emprunt`
--
ALTER TABLE `Emprunt`
  MODIFY `ID_Emprunt` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `Genre`
--
ALTER TABLE `Genre`
  MODIFY `ID_Genre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Livre`
--
ALTER TABLE `Livre`
  MODIFY `ID_Livre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Reservation`
--
ALTER TABLE `Reservation`
  MODIFY `ID_Reservation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `Utilisateur`
--
ALTER TABLE `Utilisateur`
  MODIFY `ID_Utilisateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Administrateur`
--
ALTER TABLE `Administrateur`
  ADD CONSTRAINT `administrateur_ibfk_1` FOREIGN KEY (`ID_Admin`) REFERENCES `Utilisateur` (`ID_Utilisateur`);

--
-- Contraintes pour la table `Emprunt`
--
ALTER TABLE `Emprunt`
  ADD CONSTRAINT `emprunt_ibfk_1` FOREIGN KEY (`ID_Livre`) REFERENCES `Livre` (`ID_Livre`),
  ADD CONSTRAINT `emprunt_ibfk_2` FOREIGN KEY (`ID_Utilisateur`) REFERENCES `Utilisateur` (`ID_Utilisateur`);

--
-- Contraintes pour la table `Livre`
--
ALTER TABLE `Livre`
  ADD CONSTRAINT `livre_ibfk_1` FOREIGN KEY (`ID_Collection`) REFERENCES `Collection` (`ID_Collection`),
  ADD CONSTRAINT `livre_ibfk_2` FOREIGN KEY (`ID_Auteur`) REFERENCES `Auteur` (`ID_Auteur`),
  ADD CONSTRAINT `livre_ibfk_3` FOREIGN KEY (`ID_Genre`) REFERENCES `Genre` (`ID_Genre`);

--
-- Contraintes pour la table `Reservation`
--
ALTER TABLE `Reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`ID_Livre`) REFERENCES `Livre` (`ID_Livre`),
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`ID_Utilisateur`) REFERENCES `Utilisateur` (`ID_Utilisateur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
