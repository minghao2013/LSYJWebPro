import pages
from base.web_base import WebBase
from js_ele import ele_script


class MasterAddPage(WebBase):

    # 添加大师信息
    def add_master_content(self, master_name="test1", master_pic="C:\\Users\\24453\\Desktop\\toutu.png",
                           master_horizontal_pic="C:\\Users\\24453\\Desktop\\hengtu.png",
                           master_vertical_pic="C:\\Users\\24453\\Desktop\\shutu.png",
                           master_lesson_pic="C:\\Users\\24453\\Desktop\\xinketu.png",
                           master_lesson_share_pic="C:\\Users\\24453\\Desktop\\fenxiangtu.png",
                           master_skill="1111", master_share_content="2222",
                           master_sort="-9999", master_bright_point="我是一个老师", master_desc="我是一个老师"):
        """
        :param master_name:老师名称
        :param master_pic:老师头图
        :param master_horizontal_pic:老师横图
        :param master_vertical_pic:老师竖图
        :param master_lesson_pic:老师新课图
        :param master_lesson_share_pic:老师分享图
        :param master_skill:老师技能
        :param master_share_content:老师分享内容
        :param master_sort:老师排序值,越小越靠前
        :param master_bright_point:老师课程亮点
        :param master_desc:老师简介
        """
        self.do_send_keys(pages.master_name_tag, master_name)
        self.upload_file(pages.master_pic_tag, master_pic)
        self.upload_file(pages.master_horizontal_pic_tag, master_horizontal_pic)
        self.upload_file(pages.master_vertical_pic_tag, master_vertical_pic)
        self.upload_file(pages.master_lesson_pic_tag, master_lesson_pic)
        self.upload_file(pages.master_lesson_share_pic_tag, master_lesson_share_pic)
        self.do_send_keys(pages.master_skill_tag, master_skill)
        self.do_send_keys(pages.master_share_content_tag, master_share_content)
        self.do_send_keys(pages.master_sort_tag, master_sort)
        self.do_send_keys(pages.master_bright_point_tag, master_bright_point)
        self.do_send_keys(pages.master_desc_tag, master_desc)
        self.do_execute_script(ele_script)
        # ele = self.do_find_element(pages.master_add_online_tag)

        self.do_click(pages.master_add_btn)
        return self

    # 添加成功toast提示
    def add_success_msg(self):
        return self.get_element_text(pages.master_add_success_msg)
