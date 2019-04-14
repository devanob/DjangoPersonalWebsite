-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: Personals
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ProjectUser_projectuser`
--

DROP TABLE IF EXISTS `ProjectUser_projectuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProjectUser_projectuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `gitUser` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectUser_projectuser`
--

LOCK TABLES `ProjectUser_projectuser` WRITE;
/*!40000 ALTER TABLE `ProjectUser_projectuser` DISABLE KEYS */;
INSERT INTO `ProjectUser_projectuser` VALUES (1,'pbkdf2_sha256$120000$KJTtdPBYoQnj$8MxS8C2ZD7rwCpihtsoIH2UoVTzhSXQWhdqspTBU3VI=','2019-04-11 02:33:03.000000',1,'DevanoBrown','','','browndevano@gmail.com',1,1,'2019-04-11 02:32:03.000000','devanob');
/*!40000 ALTER TABLE `ProjectUser_projectuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectUser_projectuser_groups`
--

DROP TABLE IF EXISTS `ProjectUser_projectuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProjectUser_projectuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ProjectUser_projectuser__projectuser_id_group_id_bf1c46c0_uniq` (`projectuser_id`,`group_id`),
  KEY `ProjectUser_projectu_group_id_d4b833df_fk_auth_grou` (`group_id`),
  CONSTRAINT `ProjectUser_projectu_group_id_d4b833df_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `ProjectUser_projectu_projectuser_id_55f46778_fk_ProjectUs` FOREIGN KEY (`projectuser_id`) REFERENCES `ProjectUser_projectuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectUser_projectuser_groups`
--

LOCK TABLES `ProjectUser_projectuser_groups` WRITE;
/*!40000 ALTER TABLE `ProjectUser_projectuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `ProjectUser_projectuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectUser_projectuser_user_permissions`
--

DROP TABLE IF EXISTS `ProjectUser_projectuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProjectUser_projectuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ProjectUser_projectuser__projectuser_id_permissio_b5b48df6_uniq` (`projectuser_id`,`permission_id`),
  KEY `ProjectUser_projectu_permission_id_07de2f7b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `ProjectUser_projectu_permission_id_07de2f7b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `ProjectUser_projectu_projectuser_id_580703af_fk_ProjectUs` FOREIGN KEY (`projectuser_id`) REFERENCES `ProjectUser_projectuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectUser_projectuser_user_permissions`
--

LOCK TABLES `ProjectUser_projectuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `ProjectUser_projectuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `ProjectUser_projectuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add project',6,'add_project'),(22,'Can change project',6,'change_project'),(23,'Can delete project',6,'delete_project'),(24,'Can view project',6,'view_project'),(25,'Can add contact',7,'add_contact'),(26,'Can change contact',7,'change_contact'),(27,'Can delete contact',7,'delete_contact'),(28,'Can view contact',7,'view_contact'),(29,'Can add crontab',8,'add_crontabschedule'),(30,'Can change crontab',8,'change_crontabschedule'),(31,'Can delete crontab',8,'delete_crontabschedule'),(32,'Can view crontab',8,'view_crontabschedule'),(33,'Can add interval',9,'add_intervalschedule'),(34,'Can change interval',9,'change_intervalschedule'),(35,'Can delete interval',9,'delete_intervalschedule'),(36,'Can view interval',9,'view_intervalschedule'),(37,'Can add periodic task',10,'add_periodictask'),(38,'Can change periodic task',10,'change_periodictask'),(39,'Can delete periodic task',10,'delete_periodictask'),(40,'Can view periodic task',10,'view_periodictask'),(41,'Can add periodic tasks',11,'add_periodictasks'),(42,'Can change periodic tasks',11,'change_periodictasks'),(43,'Can delete periodic tasks',11,'delete_periodictasks'),(44,'Can view periodic tasks',11,'view_periodictasks'),(45,'Can add solar event',12,'add_solarschedule'),(46,'Can change solar event',12,'change_solarschedule'),(47,'Can delete solar event',12,'delete_solarschedule'),(48,'Can view solar event',12,'view_solarschedule'),(49,'Can add user',13,'add_projectuser'),(50,'Can change user',13,'change_projectuser'),(51,'Can delete user',13,'delete_projectuser'),(52,'Can view user',13,'view_projectuser'),(53,'Can add tag',14,'add_tag'),(54,'Can change tag',14,'change_tag'),(55,'Can delete tag',14,'delete_tag'),(56,'Can view tag',14,'view_tag');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_contact`
--

DROP TABLE IF EXISTS `contact_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contact_name` varchar(100) NOT NULL,
  `contact_email` varchar(70) NOT NULL,
  `contact_phone_number` varchar(70) NOT NULL,
  `contact_message` varchar(200) NOT NULL,
  `contact_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_contact`
--

LOCK TABLES `contact_contact` WRITE;
/*!40000 ALTER TABLE `contact_contact` DISABLE KEYS */;
INSERT INTO `contact_contact` VALUES (1,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:46.050693'),(2,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:46.837520'),(3,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:47.408434'),(4,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:47.580257'),(5,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:47.727847'),(6,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:47.880916'),(7,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:48.034683'),(8,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:48.208093'),(9,'D%%','h@gmail.com','jnkjnknlk','--->zz','2019-04-11 03:52:48.713706'),(10,'Devano','lolabirch87@gmail.co','1-242-785-4539','nn','2019-04-11 03:53:11.002080'),(11,'Devano','lolabirch87@gmail.co','1-242-785-4539','nn','2019-04-11 03:53:12.479818');
/*!40000 ALTER TABLE `contact_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_ProjectUser_projectuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_ProjectUser_projectuser_id` FOREIGN KEY (`user_id`) REFERENCES `ProjectUser_projectuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-04-11 02:33:20.162534','1','DevanoBrown',2,'[{\"changed\": {\"fields\": [\"gitUser\"]}}]',13,1),(2,'2019-04-11 02:34:43.337618','1','DevanoBrown',2,'[]',13,1),(3,'2019-04-11 02:57:10.724949','DjangoPersonalWebsite','DjangoPersonalWebsite created on 02-07-2019, 03:12:09 last updated 04-04-2019, 05:03:30 ',3,'',6,1),(4,'2019-04-11 02:57:10.729663','SmallAppAssingment5','SmallAppAssingment5 created on 04-03-2019, 05:29:56 last updated 04-03-2019, 05:31:00 ',3,'',6,1),(5,'2019-04-11 02:57:10.738447','A.I-Search-','A.I-Search- created on 02-07-2019, 03:27:23 last updated 03-31-2019, 16:23:33 ',3,'',6,1),(6,'2019-04-11 02:57:10.742342','Flight-Simulator','Flight-Simulator created on 02-18-2019, 04:09:32 last updated 03-06-2019, 06:34:27 ',3,'',6,1),(7,'2019-04-11 02:57:10.746176','Personal-Assitance-Web-Application','Personal-Assitance-Web-Application created on 02-18-2019, 04:16:01 last updated 02-18-2019, 21:08:06 ',3,'',6,1),(8,'2019-04-11 03:29:21.849360','DjangoPersonalWebsite','DjangoPersonalWebsite created on 02-07-2019, 03:12:09 last updated 04-04-2019, 05:03:30 ',3,'',6,1),(9,'2019-04-11 03:29:21.854407','SmallAppAssingment5','SmallAppAssingment5 created on 04-03-2019, 05:29:56 last updated 04-03-2019, 05:31:00 ',3,'',6,1),(10,'2019-04-11 03:29:21.862825','A.I-Search-','A.I-Search- created on 02-07-2019, 03:27:23 last updated 03-31-2019, 16:23:33 ',3,'',6,1),(11,'2019-04-11 03:29:21.866744','Flight-Simulator','Flight-Simulator created on 02-18-2019, 04:09:32 last updated 03-06-2019, 06:34:27 ',3,'',6,1),(12,'2019-04-11 03:29:21.870483','Personal-Assitance-Web-Application','Personal-Assitance-Web-Application created on 02-18-2019, 04:16:01 last updated 02-18-2019, 21:08:06 ',3,'',6,1),(13,'2019-04-11 03:32:26.714633','DjangoPersonalWebsite','DjangoPersonalWebsite created on 02-07-2019, 03:12:09 last updated 04-04-2019, 05:03:30 ',3,'',6,1),(14,'2019-04-11 03:32:26.719480','SmallAppAssingment5','SmallAppAssingment5 created on 04-03-2019, 05:29:56 last updated 04-03-2019, 05:31:00 ',3,'',6,1),(15,'2019-04-11 03:32:26.723864','A.I-Search-','A.I-Search- created on 02-07-2019, 03:27:23 last updated 03-31-2019, 16:23:33 ',3,'',6,1),(16,'2019-04-11 03:32:26.731610','Flight-Simulator','Flight-Simulator created on 02-18-2019, 04:09:32 last updated 03-06-2019, 06:34:27 ',3,'',6,1),(17,'2019-04-11 03:32:26.736245','Personal-Assitance-Web-Application','Personal-Assitance-Web-Application created on 02-18-2019, 04:16:01 last updated 02-18-2019, 21:08:06 ',3,'',6,1),(18,'2019-04-11 03:47:14.580009','Systems','Systems created on 04-03-2019, 22:34:37 last updated 04-11-2019, 03:38:41 ',3,'',6,1),(19,'2019-04-11 03:47:14.587354','DjangoPersonalWebsite','DjangoPersonalWebsite created on 02-07-2019, 03:12:09 last updated 04-04-2019, 05:03:30 ',3,'',6,1),(20,'2019-04-11 03:47:14.592186','SmallAppAssingment5','SmallAppAssingment5 created on 04-03-2019, 05:29:56 last updated 04-03-2019, 05:31:00 ',3,'',6,1),(21,'2019-04-11 03:47:14.596468','A.I-Search-','A.I-Search- created on 02-07-2019, 03:27:23 last updated 03-31-2019, 16:23:33 ',3,'',6,1),(22,'2019-04-11 03:47:14.600746','Flight-Simulator','Flight-Simulator created on 02-18-2019, 04:09:32 last updated 03-06-2019, 06:34:27 ',3,'',6,1),(23,'2019-04-11 03:47:14.604998','Personal-Assitance-Web-Application','Personal-Assitance-Web-Application created on 02-18-2019, 04:16:01 last updated 02-18-2019, 21:08:06 ',3,'',6,1),(24,'2019-04-11 03:49:07.836337','thesis','thesis created on 03-16-2019, 20:57:53 last updated 04-11-2019, 03:41:59 ',3,'',6,1),(25,'2019-04-11 15:48:21.276229','Systems','Systems created on 04-03-2019, 22:34:37 last updated 04-11-2019, 03:38:41 ',3,'',6,1),(26,'2019-04-11 15:48:21.280851','SmallAppAssingment5','SmallAppAssingment5 created on 04-03-2019, 05:29:56 last updated 04-03-2019, 05:31:00 ',3,'',6,1),(27,'2019-04-11 15:49:24.357323','DjangoPersonalWebsite','DjangoPersonalWebsite created on 02-07-2019, 03:12:09 last updated 04-04-2019, 05:03:30 ',2,'[{\"changed\": {\"fields\": [\"project_image\"]}}]',6,1),(28,'2019-04-11 15:50:38.394085','A.I-Search-','A.I-Search- created on 02-07-2019, 03:27:23 last updated 03-31-2019, 16:23:33 ',2,'[{\"changed\": {\"fields\": [\"project_image\"]}}]',6,1),(29,'2019-04-11 15:50:52.022693','Flight-Simulator','Flight-Simulator created on 02-18-2019, 04:09:32 last updated 03-06-2019, 06:34:27 ',2,'[{\"changed\": {\"fields\": [\"project_image\"]}}]',6,1),(30,'2019-04-11 15:51:17.596196','ThreadPool','ThreadPool created on 02-07-2019, 05:57:19 last updated 02-22-2019, 16:24:52 ',2,'[{\"changed\": {\"fields\": [\"project_image\"]}}]',6,1),(31,'2019-04-11 15:51:38.148705','TicTacToeA.I','TicTacToeA.I created on 02-13-2019, 21:24:23 last updated 02-21-2019, 01:52:49 ',2,'[{\"changed\": {\"fields\": [\"project_image\"]}}]',6,1),(32,'2019-04-11 15:51:52.509762','Personal-Assitance-Web-Application','Personal-Assitance-Web-Application created on 02-18-2019, 04:16:01 last updated 02-18-2019, 21:08:06 ',2,'[{\"changed\": {\"fields\": [\"description\", \"project_image\"]}}]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_crontabschedule`
--

LOCK TABLES `django_celery_beat_crontabschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` DISABLE KEYS */;
INSERT INTO `django_celery_beat_crontabschedule` VALUES (1,'0','4','*','*','*','UTC');
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_intervalschedule`
--

LOCK TABLES `django_celery_beat_intervalschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictask`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_periodictask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int(10) unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  `solar_id` int(11) DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictask`
--

LOCK TABLES `django_celery_beat_periodictask` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictask` VALUES (1,'celery.backend_cleanup','celery.backend_cleanup','[]','{}',NULL,NULL,NULL,NULL,1,'2019-04-11 04:00:00.000343',1,'2019-04-11 04:02:15.247967','',1,NULL,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `django_celery_beat_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictasks`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictasks`
--

LOCK TABLES `django_celery_beat_periodictasks` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictasks` VALUES (1,'2019-04-11 03:32:04.712133');
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_solarschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_solarschedule`
--

LOCK TABLES `django_celery_beat_solarschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'contact','contact'),(4,'contenttypes','contenttype'),(8,'django_celery_beat','crontabschedule'),(9,'django_celery_beat','intervalschedule'),(10,'django_celery_beat','periodictask'),(11,'django_celery_beat','periodictasks'),(12,'django_celery_beat','solarschedule'),(14,'organizer','tag'),(6,'projects','project'),(13,'ProjectUser','projectuser'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-11 02:30:38.612755'),(2,'contenttypes','0002_remove_content_type_name','2019-04-11 02:30:38.747579'),(3,'auth','0001_initial','2019-04-11 02:30:39.021250'),(4,'auth','0002_alter_permission_name_max_length','2019-04-11 02:30:39.041668'),(5,'auth','0003_alter_user_email_max_length','2019-04-11 02:30:39.052850'),(6,'auth','0004_alter_user_username_opts','2019-04-11 02:30:39.063690'),(7,'auth','0005_alter_user_last_login_null','2019-04-11 02:30:39.074935'),(8,'auth','0006_require_contenttypes_0002','2019-04-11 02:30:39.081076'),(9,'auth','0007_alter_validators_add_error_messages','2019-04-11 02:30:39.093313'),(10,'auth','0008_alter_user_username_max_length','2019-04-11 02:30:39.103951'),(11,'auth','0009_alter_user_last_name_max_length','2019-04-11 02:30:39.115106'),(12,'ProjectUser','0001_initial','2019-04-11 02:30:39.436027'),(13,'ProjectUser','0002_projectuser_gituser','2019-04-11 02:30:39.494562'),(14,'ProjectUser','0003_auto_20190313_1728','2019-04-11 02:30:39.508498'),(15,'admin','0001_initial','2019-04-11 02:30:39.660320'),(16,'admin','0002_logentry_remove_auto_add','2019-04-11 02:30:39.674826'),(17,'admin','0003_logentry_add_action_flag_choices','2019-04-11 02:30:39.688870'),(18,'contact','0001_initial','2019-04-11 02:30:39.722262'),(19,'contact','0002_auto_20190407_0336','2019-04-11 02:30:39.855874'),(20,'contact','0003_contact_contact_date','2019-04-11 02:30:39.899566'),(21,'django_celery_beat','0001_initial','2019-04-11 02:30:41.122821'),(22,'django_celery_beat','0002_auto_20161118_0346','2019-04-11 02:30:41.256453'),(23,'django_celery_beat','0003_auto_20161209_0049','2019-04-11 02:30:41.285317'),(24,'django_celery_beat','0004_auto_20170221_0000','2019-04-11 02:30:41.296198'),(25,'django_celery_beat','0005_add_solarschedule_events_choices','2019-04-11 02:30:41.506935'),(26,'django_celery_beat','0006_auto_20180210_1226','2019-04-11 02:30:41.512290'),(27,'django_celery_beat','0006_auto_20180322_0932','2019-04-11 02:30:41.517441'),(28,'django_celery_beat','0007_auto_20180521_0826','2019-04-11 02:30:41.522351'),(29,'django_celery_beat','0008_auto_20180914_1922','2019-04-11 02:30:41.527112'),(30,'django_celery_beat','0006_periodictask_priority','2019-04-11 02:30:41.583739'),(31,'organizer','0001_initial','2019-04-11 02:30:41.616751'),(32,'organizer','0002_auto_20190219_1817','2019-04-11 02:30:41.667758'),(33,'projects','0001_initial','2019-04-11 02:30:41.719861'),(34,'projects','0002_delete_project','2019-04-11 02:30:41.735718'),(35,'projects','0003_project','2019-04-11 02:30:41.781155'),(36,'projects','0004_auto_20190219_0242','2019-04-11 02:30:41.880484'),(37,'projects','0005_project_description','2019-04-11 02:30:41.926378'),(38,'projects','0006_project_prokject_link','2019-04-11 02:30:41.972851'),(39,'projects','0007_auto_20190219_0301','2019-04-11 02:30:42.118173'),(40,'projects','0008_auto_20190219_1750','2019-04-11 02:30:42.126642'),(41,'projects','0009_project_tags','2019-04-11 02:30:42.285144'),(42,'projects','0010_auto_20190220_0423','2019-04-11 02:30:42.298041'),(43,'projects','0011_auto_20190220_0432','2019-04-11 02:30:42.330298'),(44,'projects','0012_auto_20190220_1439','2019-04-11 02:30:42.341262'),(45,'projects','0013_auto_20190313_0705','2019-04-11 02:30:42.355803'),(46,'projects','0014_auto_20190313_0719','2019-04-11 02:30:42.370163'),(47,'projects','0015_project_projecthandlier','2019-04-11 02:30:42.489421'),(48,'projects','0016_auto_20190314_0008','2019-04-11 02:30:42.624845'),(49,'projects','0017_project_project_image','2019-04-11 02:30:42.690815'),(50,'projects','0018_auto_20190331_0747','2019-04-11 02:30:42.711675'),(51,'projects','0019_auto_20190331_0754','2019-04-11 02:30:42.728360'),(52,'projects','0020_auto_20190331_0824','2019-04-11 02:30:42.744879'),(53,'projects','0021_auto_20190407_0327','2019-04-11 02:30:42.877230'),(54,'sessions','0001_initial','2019-04-11 02:30:42.924912'),(55,'django_celery_beat','0005_add_solarschedule_events_choices_squashed_0009_merge_20181012_1416','2019-04-11 02:30:42.933047');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('n6dclocr6c3lxdowzgjj5tdhbehr4ftp','OTIyM2QxZjIyNjhkYjk2Mzc5ODkwODEwN2E1MTZhNjQyMWRlMDMxMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiN2MxYTRlZmFiNGVkYWNiMTU3YWY2OTRjY2YxYzhiOGI0N2MyMTQyIn0=','2019-04-25 02:33:03.247226');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizer_tag`
--

DROP TABLE IF EXISTS `organizer_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organizer_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(31) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `organizer_tag_slug_18f41d77` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizer_tag`
--

LOCK TABLES `organizer_tag` WRITE;
/*!40000 ALTER TABLE `organizer_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `organizer_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project`
--

DROP TABLE IF EXISTS `projects_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_project` (
  `projectName` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `imglink` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `project_link` varchar(100) NOT NULL,
  `projectHandlier_id` int(11) NOT NULL,
  `project_image` varchar(100) NOT NULL,
  PRIMARY KEY (`projectName`),
  UNIQUE KEY `projects_project_project_name_8c908fd9_uniq` (`projectName`),
  KEY `projects_project_slug_2d50067a` (`slug`),
  KEY `projects_project_projectHandlier_id_58c6e919_fk_ProjectUs` (`projectHandlier_id`),
  CONSTRAINT `projects_project_projectHandlier_id_58c6e919_fk_ProjectUs` FOREIGN KEY (`projectHandlier_id`) REFERENCES `ProjectUser_projectuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project`
--

LOCK TABLES `projects_project` WRITE;
/*!40000 ALTER TABLE `projects_project` DISABLE KEYS */;
INSERT INTO `projects_project` VALUES ('A.I-Search-','ai-search','2019-02-07 03:27:23.000000','2019-03-31 16:23:33.000000','A.I-Search-.jpg','These is a project consisting of various search methods used in an n*n slide puzzle written in C++','https://github.com/devanob/A.I-Search-',1,'img/project_img/TicTacToeA.I_TJ2X6zZ.jpg'),('DjangoPersonalWebsite','djangopersonalwebsite','2019-02-07 03:12:09.000000','2019-04-04 05:03:30.000000','DjangoPersonalWebsite.jpg','DjangoPersonalWebsite','https://github.com/devanob/DjangoPersonalWebsite',1,'img/project_img/DjangoPersonalWebsite_AZSBBR7.jpg'),('Flight-Simulator','flight-simulator','2019-02-18 04:09:32.000000','2019-03-06 06:34:27.000000','Flight-Simulator.jpg','This is Fight Simulator written in C++ and OpenGl. This  Will Be Updated Or Another With Repository For OpenGl 4+','https://github.com/devanob/Flight-Simulator',1,'img/project_img/Flight-Simulator_WXCMtpY.png'),('Personal-Assitance-Web-Application','personal-assitance-web-application','2019-02-18 04:16:01.000000','2019-02-18 21:08:06.000000','Personal-Assitance-Web-Application.jpg','This Web Application Written Node.Js, Front End Javascript, CSS, HMTL, JQuery. Single Page App. This application was written For  NorthWood Client As Part As An OpenSource Application. Feature Real Time Messaging, Memos, Live Event Handier, Relaxation. This Application was created with the elderly in mind. With Block Text, Static Non-Flashing Colours. Styling Can Easily Be Overrided With  Css','https://github.com/devanob/Personal-Assitance-Web-Application',1,'img/project_img/Personal-Assitance-Web-Application_m42Re4N.jpg'),('ThreadPool','threadpool','2019-02-07 05:57:19.000000','2019-02-22 16:24:52.000000','ThreadPool.jpg','C++ Generic C++ ThreadPool Implementation. Good For Non Blocking Task. Work In Progress','https://github.com/devanob/ThreadPool',1,'img/project_img/ThreadPool_lPNSgiM.jpg'),('TicTacToeA.I','tictactoeai','2019-02-13 21:24:23.000000','2019-02-21 01:52:49.000000','TicTacToeA.I.jpg','Making An A.I System For Tic Tac Toe. This Was Implementing A MiniMax.','https://github.com/devanob/TicTacToeA.I',1,'img/project_img/TicTacToeA.I_riTr18n.jpg');
/*!40000 ALTER TABLE `projects_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project_tags`
--

DROP TABLE IF EXISTS `projects_project_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_project_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` varchar(255) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `projects_project_tags_project_id_tag_id_5891719a_uniq` (`project_id`,`tag_id`),
  KEY `projects_project_tags_tag_id_c949773d_fk_organizer_tag_id` (`tag_id`),
  CONSTRAINT `projects_project_tag_project_id_9bbfa17b_fk_projects_` FOREIGN KEY (`project_id`) REFERENCES `projects_project` (`projectName`),
  CONSTRAINT `projects_project_tags_tag_id_c949773d_fk_organizer_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `organizer_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project_tags`
--

LOCK TABLES `projects_project_tags` WRITE;
/*!40000 ALTER TABLE `projects_project_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_project_tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-11 20:39:20
