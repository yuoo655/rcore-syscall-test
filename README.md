# how

把文件放在os目录下. 保证在os目录下make run能运行测试

自动评分脚本会先执行sh runos.sh把运行结果存在output文件中

test.py通过判断output文件中Pass!的数量来统计通过的测例
