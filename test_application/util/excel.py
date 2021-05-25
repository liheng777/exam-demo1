# 首先逻辑判断是搜索页面还是默认全部显示页面,全部显示页面poemer值为None,导出全部,搜索页面导出某一个诗人数据 poemer会有值
def export_excel(self, poemer):
    par_path = path.join(BASE_DIR, 'static/xlsxfiles')
    os.chdir(par_path)
    if poemer:
        file = poemer + '.xlsx'
        # 删除昨日执行文件
        if os.path.isfile(file):
            os.remove(file)
        data = self.per_poemer_data(poemer)
    else:
        file = 'all_poemers.xlsx'
        if os.path.isfile(file):
            os.remove(file)
        data = self.all_poemers_data()
    fields = ['id', 'chaodai', 'poemer', 'zuopins_total', 'poemer_url']
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet('data')
    # 表头格式
    format1 = workbook.add_format(
        {'bold': True, 'font_color': 'black', 'font_size': 13, 'align': 'left', 'font_name': u'宋体'})
    # 表头外格式
    format2 = workbook.add_format({'font_color': 'black', 'font_size': 9, 'align': 'left', 'font_name': u'宋体'})
    # A列列宽设置能更好的显示
    worksheet.set_column("A:A", 9)
    # 插入第一行表头标题
    for i in range(0, len(fields)):
        field = fields[i]
        worksheet.write(0, i, field, format1)
    # 从第二行开始插入数据
    for i in range(len(data)):
        item = data[i]
        for j in range(len(fields)):
            field = fields[j]
            worksheet.write(i + 1, j, item[field], format2)
    workbook.close()
    alert_text = '导出%s条数据到excel成功' % len(data)
    return alert_text