# 线上课checkbox执行script
ele_script = "$(\".checkbox-inline [value='1']\").click()"
# 获取用户的搜索结果
get_assert_msg_by_js = 'return document.querySelector(\".table-bordered tbody td:nth-child(2)\").innerText'
# 设置用户会期的时间控件
vip_user_view_date = 'document.querySelector(\'[name=\"view_end_date\"]\').value=\"2022-10-08\"'
