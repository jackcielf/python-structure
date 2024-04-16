# APENAS EXEMPLO

CREATE SCHEMA `nome_do_banco_de_dados`;

USE `nome_do_banco_de_dados`;

CREATE TABLE `nome_do_banco_de_dados`.`nome_da_tabela` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `id_user_UNIQUE` (`id_user` ASC),
  PRIMARY KEY (`id_user`))
ENGINE = InnoDB;
