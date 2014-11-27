CREATE TABLE `download` (
	`filename` varchar(255) NOT NULL,
	`dldate` DATETIME,
	`stats` int(11) NOT NULL,
	PRIMARY KEY  (`filename`)
)