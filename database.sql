create database if not exists fabiaoqing;
use fabiaoqing;

# 创建类别表
create table if not exists category
(
    objectId   varchar(16)  not null comment '主键' primary key,
    name       varchar(255) not null comment '类别名称',
    `order`    int          not null comment '次序',
    createTime datetime     not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime     not null on update CURRENT_TIMESTAMP comment '更新时间'
);

# 创建分组表
create table if not exists `group`
(
    objectId   varchar(16)             not null comment '主键' primary key,
    name       varchar(255) default '' not null comment '分组名称',
    parentId   varchar(16)  default '' not null comment '类别id',
    `order`    int                     not null comment '次序',
    createTime datetime                not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime                not null on update CURRENT_TIMESTAMP comment '更新时间'
);

# 创建表情表
create table if not exists emoticon
(
    objectId   varchar(16)             not null comment '主键' primary key,
    name       varchar(255) default '' not null comment '表情包名称',
    url        varchar(255)            not null comment '表情包地址',
    parentId   varchar(16)  default '' not null comment '表情包的分组id',
    `order`    int                     not null comment '次序',
    createTime datetime                not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime                not null on update CURRENT_TIMESTAMP comment '更新时间'
);