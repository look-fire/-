# coding: utf-8

import json
from configs.orm_db import lorm_pool_57, lorm_pool as lorm_pool_yh
from configs import dbconfig as conn
from common.common import Struct
from configs import db56config as db_56, dbconfig as db_57

creat_sql = """
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_class_performance
-- ----------------------------
DROP TABLE IF EXISTS `user_class_performance`;
CREATE TABLE `user_class_performance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `attendance_detail_id` int(11) NOT NULL DEFAULT '0' COMMENT '学生考勤id',
  `json_data_good` json NOT NULL COMMENT '学生良好表现  {"注意力集中":["17:30", "17.35", "18:00"], "学习用心":["17.37"]}',
  `json_data_bad` json DEFAULT NULL COMMENT '学生不良表现\r\n{"注意力集中":["17:30", "17.35", "18:00"], "学习用心":["17.37"]}',
  `json_data_tea` json DEFAULT NULL COMMENT '教师评语  [{"content": "哈哈哈哈哈", "add_time":"17:38"}]',
  `good_num` int(2) NOT NULL DEFAULT '0' COMMENT '良好表现数量',
  `bad_num` int(2) NOT NULL DEFAULT '0' COMMENT '不良表现数量',
  `total_num` int(2) NOT NULL DEFAULT '0' COMMENT '表现合计数量  total_num = good_num - bad_num',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '是否在学生端展示课堂表现弹窗  0 不展示   1 展示 -1 已展示',
  `add_time` int(11) NOT NULL DEFAULT '0' COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for user_communication
-- ----------------------------
DROP TABLE IF EXISTS `user_communication`;
CREATE TABLE `user_communication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stu_id` int(11) NOT NULL COMMENT '用户id',
  `class_id` int(5) NOT NULL COMMENT '学生班级id',
  `class_time` int(11) NOT NULL DEFAULT '0' COMMENT '班级上课时间',
  `attendance_detail_id` int(11) NOT NULL DEFAULT '0' COMMENT '学生考勤记录',
  `stu_com_tea_id` int(11) NOT NULL DEFAULT '0' COMMENT '与学生沟通的教师ID',
  `stu_status` int(2) NOT NULL DEFAULT '0' COMMENT '与学生沟通状态 0 待沟通 1 已沟通 2 未沟通',
  `stu_com_time` int(11) NOT NULL DEFAULT '0' COMMENT '与学生沟通时间',
  `par_com_tea_id` int(11) NOT NULL DEFAULT '0' COMMENT '与家长沟通的教师ID',
  `par_status` int(2) NOT NULL DEFAULT '0' COMMENT '与家长沟通状态 0 待沟通 1 已沟通 2 未沟通',
  `par_com_time` int(11) NOT NULL DEFAULT '0' COMMENT '与家长沟通时间',
  `photo_url` varchar(100) NOT NULL COMMENT '照片url',
  `par_com_jms_id` int(11) NOT NULL DEFAULT '0' COMMENT '与家长沟通的管理员ID',
  `is_comments` int(2) NOT NULL DEFAULT '0' COMMENT '教师是否点评  在学情分析列表中使用  0未批改  1课外沟通  2需要面对面沟通，3需要平板沟通',
  `add_time` int(11) NOT NULL DEFAULT '0' COMMENT '添加时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for user_current_catalog
-- ----------------------------
DROP TABLE IF EXISTS `user_current_catalog`;
CREATE TABLE `user_current_catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `book_id` int(5) NOT NULL COMMENT '教材id',
  `user_book_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户教材记录id',
  `catalog_id` int(5) NOT NULL DEFAULT '0' COMMENT '课时id',
  `mystic_position` int(5) NOT NULL DEFAULT '0' COMMENT '神秘关卡位置 0 没有神秘关卡  1 (两关)提交作业  2 (两关)知识温习  3 （两关）通关  6 (一关)提交作业  7 (一关)知识温习  8（一关）通关',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for user_device
-- ----------------------------
DROP TABLE IF EXISTS `user_device`;
CREATE TABLE `user_device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `device_id` varchar(30) NOT NULL DEFAULT '' COMMENT '设备id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for user_message
-- ----------------------------
DROP TABLE IF EXISTS `user_message`;
CREATE TABLE `user_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `user_book_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户教材表id',
  `test_id` int(11) NOT NULL DEFAULT '0' COMMENT '主测试id',
  `class_id` int(5) NOT NULL DEFAULT '0' COMMENT '班级id',
  `msg_type` int(2) NOT NULL DEFAULT '0' COMMENT '类型                     msg_type值            content字段结构\r\n 请求解锁新课时                     11        {"stu_id": 123,"stu_name": "张三", "cid": 11,"c_name": "有理数的加法\r\n停留时间过长(安卓调用报警接口)      12        {"stu_id": 123,"stu_name": "张三"}\r\n未按要求学习(安卓调用报警接口)      13        {"stu_id": 123,"stu_name": "张三"}\r\n 再次闯关错题数过多                 14        {"stu_id": 123,"stu_name": "张三"}\r\n\r\n普通第二关批改                     16          空\r\n普通第三关批改                     17          空\r\n普通四五六/章末/实验三四批改        18          空\r\n实验第二关批改                     19          空\r\n        \r\n调整学习起点                       31         {"cid": 11,"c_name": "有理数的加法"}\r\n下课                                       34         空',
  `content` json DEFAULT NULL COMMENT '消息内容',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '0 未处理 -1 已处理/删除',
  `add_time` int(11) NOT NULL DEFAULT '0' COMMENT '添加时间',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=950 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for experiment_study
-- ----------------------------
DROP TABLE IF EXISTS `experiment_study`;
CREATE TABLE `experiment_study` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL COMMENT '主测试id',
  `exp_id` int(11) NOT NULL COMMENT '实验id',
  `json_data` json DEFAULT NULL COMMENT '所有空的个数',
  `status` int(2) NOT NULL COMMENT '关卡状态0:未过关 1:过关',
  `add_time` int(11) NOT NULL COMMENT '添加时间',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for experiment_understand
-- ----------------------------
DROP TABLE IF EXISTS `experiment_understand`;
CREATE TABLE `experiment_understand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL COMMENT '主测试id',
  `exp_id` int(5) DEFAULT '0' COMMENT '实验id',
  `json_data_1` json DEFAULT NULL COMMENT '测试1记录\r\n[{''q_id'':11, ''status'': 2, ''test_num'': 4}]\r\n    q_id: 试题id；status:试题首次作答状态，1 正确  2 错误；test_num:试题测试次数',
  `json_data_2` json DEFAULT NULL COMMENT '测试2记录\r\n[{''q_id'':11, ''status'': 2, ''test_num'': 4}]\r\n    q_id: 试题id；status:试题首次作答状态，1 正确  2 错误；test_num:试题测试次数',
  `status` int(2) NOT NULL DEFAULT '0' COMMENT '测试状态',
  `add_time` int(11) NOT NULL COMMENT '添加时间',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

DROP TABLE IF EXISTS `current_catalog`;

DROP TABLE IF EXISTS `experiment_apply_test`;

DROP TABLE IF EXISTS `experiment_test`;

alter table analysis add user_book_id int(11) not null default 0 comment '学生教材', add is_focus int(11) not null default 2 comment '重点学生',
add original_class_id int(11) not null default 0 comment '原班级',  add personalise_status json  comment '个性化作业提交状态' ,
add study_progress json comment '学习进度', add single_study varchar(10) not null default "0" comment '单次学习进度', 
add total_study varchar(10) not null default "0" comment '总体学习进度',
add study_analysis json comment '学习轨迹分析', add update_time int(11) not null default 0 comment '生成时间',
add study_lesson json comment '学习效果', add teach_effect json comment '教学效果'  ;  # 学情分析表

alter table analysis drop column habit, drop column attitude, drop column ability, drop column effect, drop column d_json_data;  # 删除无效字段

alter table analysis_statistics add clear_status int(11) not null default 0 comment '是否是本次课通关',
add level_score json comment '各关学习分数',
add level_analysis json comment '学习效果分析';
alter table analysis_statistics change type c_type int(11);

alter table personalise_statistics change type c_type int(11);

alter table attendance add down_time int(11) not null default 0 comment '下课时间', add tea_user_id int(11) not null default 0 comment '教课老师';

alter table attendance_detail add is_best int(11) not null default 0 comment '最佳表现', add original_class_id int(11) not null default 0 comment '原班级', 
add user_book_id int(11) not null default 0 comment '学生教材', add used_lesson_num int(11) not null default 0 comment '本次课消课数量', 
add curr_lesson_num int(11) not null default 0 comment '已经使用课时数', add total_lesson_num int(11) not null default 0 comment '消课课时',
add par_com_of_month int(11) not null default 0 comment '已经使用课时数', 
add mystic_homework int(11) not null default 0 comment '是否完成神秘关卡作业提交';

alter table mystic add user_book_id int(11) not null default 0 comment '学生教材',  add attendance_detail_id int(11) not null default 0 comment '考勤id' ;

alter table knowledge_dictation  add update_time int(11) not null default 0 comment '更新时间' ;

alter table personalise add original_class_id int(11) not null default 0 comment '原班级', add user_book_id int(11) not null default 0 comment '学生教材';
alter table personalise alter column is_sign set default '-1', alter column homework_status set default 0, 
alter column position set default 2, alter column correct_time set default 0, alter column make_status set default 0;

alter table test add clear_time int(11) not null default 0 comment '章节完成时间', add user_book_id int(11) not null default 0 comment '学生教材' ;

alter table user_extend change head head_url varchar(100);

alter table user_jump_catalog add user_book_id int(11) not null default 0 comment '学生教材';
alter table user_jump_catalog change gt_msg_id user_msg_id int(11);

alter table weak add user_book_id int(11) not null default 0 comment '学生教材', add test_id int(11) not null default 0 comment '主测试id',add attendance_detail_id int(11) not null default 0 comment '考勤id';

UPDATE analysis SET original_class_id=class_id;

UPDATE attendance_detail SET original_class_id=class_id;

UPDATE personalise SET original_class_id=class_id;

"""


def get_table_name(db_name):
    """
    获取数据库下的所有表名
    :return:
    """
    sql = "select table_name  from information_schema.tables where table_schema = '{db_name}' and table_type = 'base table';".format(
        db_name=db_name)
    result = conn.fetchall_to_dict(db_name, sql)
    return result


def rename_table_name(db_name, mark):
    """
    重命名表名
    :param db_name
    :param mark
    :return:
    """
    # 1 重命名表名
    print("<<<<开始{mark}重命名表名：".format(mark=mark))
    tables = get_table_name(db_name)  # 获取数据库下的所有表名
    for table in tables:
        old_table = table.get("table_name", "")
        if old_table.startswith("{}".format(mark)):
            new_t_name = old_table[3:]
            print("{old_table} 重命名为：{new_t_name}".format(old_table=old_table, new_t_name=new_t_name))
            sql = "rename table {t_name} to {new_t_name};".format(
                t_name=old_table, new_t_name=new_t_name)
            conn.exec_sql(db_name, sql)
    print(">>>>Done")


def alter_test(test, db_name, yh_db_name, project_id):
    """
    更改test 表中的position level_id level_status, user_book_id 字段值
    :param test:
    :param db_name:
    :param yh_db_name:
    :param project_id:
    :return:
    """
    level_id = test.get("level_id") + 1 if test.get("level_status") == 1 else test.get("level_id")
    test_level = test.get("level_id")
    test_position = test.get("position")
    position = (test.get("position") + 1) if test.get("position") > 5 else test.get("position")
    if test_level == 2 and test_position == 3:
        position = 2
    elif test_level == 3 and test_position in (3, 8):
        position = 2
    elif test_level >= 4:
        # position = 2 if test_position in (3, 4) else 8 if test_position in (8, 9) else test_position
        position = 2 if test_position in (3, 4, 8, 9) else test_position  # 所有带批改的流程从错题订正重新走
    if test.get("level_status") == 1 and test.get("position") == 1:
        position = 0

    clear_time = test.get("update_time") if (test.get("c_type") == 3 and test.get("level_id") > 3) or (
        test.get("c_type") == 1 and test.get("level_id") > 4) else 0

    # 查询用户使用的教材对应的用户教材ID（user_book_id）
    yh_conn = lorm_pool_yh(yh_db_name)  # 指定要连接的数据库(YH 库)
    result = yh_conn.default.yh_user_book.filter(user_id=test.get("user_id"), book_id=test.get("book_id"),
                                                 project_id=project_id, status__in=[0, 1, 2]).select("id")[:]
    user_book_id = result[-1].get("id") if len(result) > 0 else 0
    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库（逻辑库）
    lore_conn.default.test.filter(id=test.get("id")).update(level_status=0, level_id=level_id, position=position,
                                                            clear_time=clear_time, user_book_id=user_book_id)


def alter_knowledge(knowledge, db_name):
    """
    knowledge_dictation 表中的json_data 字段值加 值对像
    :param knowledge:
    :return:
    """
    test_ids = [one.get("test_id") for one in knowledge]
    test_ids = sorted(set(test_ids), key=test_ids.index)
    konwledge_dict = dict()
    for t_id in test_ids:
        json_list = list()
        for k in knowledge:
            if k.get("test_id") == t_id:
                temp_dict = dict(test_num=k.get("test_num"), json_data=k.get("json_data"))
                json_list.append(temp_dict)
        konwledge_dict[t_id] = json_list

    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库（逻辑库）
    lore_conn.default.knowledge_dictation.filter(test_num__gt=1).delete()  # 查询出数据之后删除无用的数据
    #  生成一组新的数据
    new_list = list()
    for key, value in konwledge_dict.items():
        new_dict = Struct()
        new_dict.test_id = key
        test_num_list = [obj.get("test_num") for obj in value]
        max_t_num = max(test_num_list)
        f_json = next((one.get("json_data") for one in value if one.get("test_num") == 1), None)
        f_json = json.loads(f_json)
        if max_t_num == 1 and not f_json:
            f_json = f_json
        else:
            for one in value:
                json_data = json.loads(one.get("json_data"))
                for k_json in json_data:
                    k_dict = next(k for k in f_json if k.get("k_id") == k_json.get("k_id"))
                    k_dict["result"] = k_json.get("result")
                    k_dict["status"] = k_json.get("status")
                    k_dict["dictation_num"] = one.get("test_num")
        new_dict.f_json = f_json
        new_list.append(new_dict)
        f_json = json.dumps(f_json)

        lore_conn.default.knowledge_dictation.filter(test_id=key, test_num=1).update(json_data=f_json,
                                                                                     test_num=max_t_num)


def alter_method(method, db_name):
    """
    method_study 表中 q_json_data 添加字段result  -1 不用温习 0 未温习 1 已温习
    :param method:
    :return:
    """
    q_json_data = method.get("q_json_data")
    q_json_data = json.loads(q_json_data)
    for one in q_json_data:
        one["result"] = 1 if one.get("status") == 2 else -1
    q_json_data = json.dumps(q_json_data)
    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库（逻辑库）
    lore_conn.default.method_study.filter(id=method.get("id")).update(q_json_data=q_json_data)


def alter_apply(apply, db_name):
    """
    apply_test 表中 json_data 添加字段q_no, ask_no
    :param method:
    :return:
    """
    q_json_data = apply.get("json_data")
    q_json_data = json.loads(q_json_data)
    # 将试题提交记录到表里
    apply_q_ids = [int(q.get("q_id")) for q in q_json_data]
    q_ids = sorted(set(apply_q_ids), key=apply_q_ids.index)  # 大题id 去重
    for i, one_q in enumerate(q_ids, start=1):
        ask_no = 1
        for one_json in q_json_data:
            if one_json.get("q_id") == one_q:
                one_json["q_no"] = i
                one_json["ask_no"] = ask_no
                ask_no += 1
            if one_json["type"] == 1 and one_json["result"] == 2:
                one_json["result"] = 0  # 待批改的状态改为未订正
    q_json_data = json.dumps(q_json_data)
    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库（逻辑库）
    lore_conn.default.apply_test.filter(id=apply.get("id")).update(json_data=q_json_data)


def __get_user_book_id(user_id, book_id, project_id, yh_db_name):
    """
    获取user_book_id
    :param user_id:
    :param book_id:
    :param project_id:
    :return:
    """
    # 查询用户使用的教材对应的用户教材ID（user_book_id）
    yh_conn = lorm_pool_yh(yh_db_name)  # 指定要连接的数据库(YH 库)
    result = yh_conn.default.yh_user_book.filter(user_id=user_id, book_id=book_id,
                                                 project_id=project_id, status__in=[0, 1, 2]).select("id")[:]
    user_book_id = result[-1].get("id") if len(result) > 0 else 0

    return user_book_id


def __get_test_id(user_id, catalog_id, book_id, db_name):
    """
    获取user_book_id
    :param user_id:
    :param catalog_id:
    :param book_id:
    :param yh_db_name:
    :return:
    """
    # 查询用户使用的教材对应的用户教材ID（user_book_id）
    yh_conn = lorm_pool_57(db_name)  # 指定要连接的数据库(YH 库)
    result = yh_conn.default.test.filter(user_id=user_id, book_id=book_id, catalog_id=catalog_id).select("id")[:]
    test_id = result[-1].get("id") if len(result) > 0 else 0

    return test_id


def update_user_book_id(db_name, yh_db_name, project_id):
    """
    更新表中的user_book_id 字段
    :param db_name:
    :param yh_db_name:
    :param project_id:
    :return:
    """
    key = lambda d: (d["user_id"], d["book_id"])
    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库
    print("正在更新analysis 表的user_book_id 字段....")
    result1 = lore_conn.default.analysis.filter(id__gt=0).select('user_id', 'book_id')[:]
    result1 = list(dedupe(result1, key))
    for obj in result1:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        lore_conn.default.analysis.filter(user_id=obj.get("user_id"), book_id=obj.get("book_id")).update(
            user_book_id=user_book_id)

    print("正在更新attendance_detail 表的user_book_id 字段....")
    result2 = lore_conn.default.attendance_detail.filter(id__gt=0).select('user_id', 'book_id')[:]
    result2 = list(dedupe(result2, key))
    for obj in result2:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        lore_conn.default.attendance_detail.filter(user_id=obj.get("user_id"), book_id=obj.get("book_id")).update(
            user_book_id=user_book_id)

    print("正在更新personalise 表的user_book_id 字段....")
    result3 = lore_conn.default.personalise.filter(id__gt=0).select('user_id', 'book_id')[:]
    result3 = list(dedupe(result3, key))
    for obj in result3:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        lore_conn.default.personalise.filter(user_id=obj.get("user_id"), book_id=obj.get("book_id")).update(
            user_book_id=user_book_id)

    print("正在更新mystic 表的user_book_id 字段....")
    result4 = lore_conn.default.mystic.filter(id__gt=0).select('user_id', 'book_id')[:]
    result4 = list(dedupe(result4, key))
    for obj in result4:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        lore_conn.default.mystic.filter(user_id=obj.get("user_id"), book_id=obj.get("book_id")).update(
            user_book_id=user_book_id)

    print("正在更新user_jump_catalog 表的user_book_id 字段....")
    result5 = lore_conn.default.user_jump_catalog.filter(id__gt=0).select('user_id', 'book_id')[:]
    result5 = list(dedupe(result5, key))
    for obj in result5:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        lore_conn.default.user_jump_catalog.filter(user_id=obj.get("user_id"), book_id=obj.get("book_id")).update(
            user_book_id=user_book_id)

    print("正在更新weak 表的user_book_id 字段....")
    result6 = lore_conn.default.weak.filter(id__gt=0).select('id', 'user_id', 'book_id', 'catalog_id')[:]
    for obj in result6:
        user_book_id = __get_user_book_id(obj.get("user_id"), obj.get("book_id"), project_id, yh_db_name)
        test_id = __get_test_id(obj.get("user_id"), obj.get("catalog_id"), obj.get("book_id"), db_name)
        lore_conn.default.weak.filter(id=obj.get("id")).update(user_book_id=user_book_id, test_id=test_id)

    print("删除weak 表中的book_id 字段")
    db_57.exec_sql(conf.get("db_name"), "alter table weak drop column book_id;")

    print("done...")


def dedupe(items, key=None):
    """
    字典列表去重

    :param items:字典列表
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def copy_date(conf):
    """
    SLH 项目数据迁移
    :return:
    """
    import time
    print("start...")
    start = int(time.time())
    db_name = conf.get("db_name")
    yh_db_name = conf.get("yh_db_name")
    project_id = conf.get("project_id")

    # 2 更改test 表中的position level_id level_status , user_book_id字段值
    lore_conn = lorm_pool_57(db_name)  # 指定要连接的数据库
    result = lore_conn.default.test.filter(id__gt=0).select('id', 'user_id', 'book_id',
                                                            'level_id',
                                                            'level_status', 'c_type',
                                                            'position', 'update_time')[:]
    print("开始修改主测试表字段...")
    for test in result:
        alter_test(test, db_name, yh_db_name, project_id)

    # 3 第二关添加字段 knowledge_dictation 表中的json_data 字段值加 值对像( 合并数据)
    print("开始修改第二关知识默写表字段...")
    t_result = lore_conn.default.knowledge_dictation.filter(id__gt=0).select("id", "test_id", "test_num", "json_data")
    alter_knowledge(t_result, db_name)

    # 4 第三关q_json_data 添加字段result  -1 不用温习 0 未温习 1 已温习
    m_result = lore_conn.default.method_study.filter(id__gt=0).select("id", "q_json_data")
    print("开始修改第三关方法学习表字段...")
    for method in m_result:
        alter_method(method, db_name)

    # 5 四五六关 添加题号记录
    q_result = lore_conn.default.apply_test.filter(id__gt=0).select("id", "json_data")
    print("开始修改四五六关 的测试提交记录 字段...")
    for apply in q_result:
        alter_apply(apply, db_name)

    # 6 update_user_book_id 更新添加user_book_id 字段
    print("*******为以下表更新真实的user_book_id值*******")
    update_user_book_id(db_name, yh_db_name, project_id)

    totTime = time.time() - start
    print("数据迁移完成， 共用时：", totTime)


if __name__ == "__main__":

    hx_conf = dict(db_name="yh_tb_hx2", yh_db_name="youhong", mark="hx_", project_id=4)
    wl_conf = dict(db_name="yh_tb_wl2", yh_db_name="youhong", mark="wl_", project_id=3)
    conf_list = [wl_conf, hx_conf]
    # wl_conf = dict(db_name="lu", yh_db_name="youhong", mark="wl_", project_id=3)
    # hx_conf = dict(db_name="hx_t", yh_db_name="youhong", mark="hx_", project_id=4)
    # conf_list = [hx_conf]  # 本地调试

    for conf in conf_list:
        # step1 : 重命名表名 ---执行方法 rename_table_name（）
        rename_table_name(conf.get("db_name"), conf.get("mark"))

        # step2 : 添加缺失字段（删除多余字段）添加表 ---执行sql文件
        """执行sql 语句"""
        # db_57.exec_sql(conf.get("db_name"), creat_sql)
        db_57.exec_sql_statements(conf.get("db_name"), creat_sql)

    for conf in conf_list:
        # step3 : 表结构更新 --- 执行方法 copy_date(conf)
        copy_date(conf)
