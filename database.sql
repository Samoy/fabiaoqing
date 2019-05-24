create database if not exists biaoqing;
use biaoqing;
# 创建类别表
create table if not exists category
(
    id    int auto_increment primary key,
    name  varchar(255) default '' not null,
    alias varchar(255) default '' not null,
    create_time datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    constraint UNIQUE_NAME_ALIAS
        unique (name, alias)
);

# 创建分组表
create table if not exists `group`
(
    id       int auto_increment primary key,
    name     varchar(255) default '' not null,
    category varchar(255) default '' not null,
    create_time datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    constraint UNIQUE_NAME_CATEGORY unique (name, category)
);

# 创建表情表
create table if not exists emoticon
(
    id    int auto_increment primary key,
    name  varchar(255) default '' not null,
    url   varchar(255) default '' not null,
    title varchar(255) default '' not null,
    create_time datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    constraint UNIQUE_NAME_TITLE unique (name, title)
);