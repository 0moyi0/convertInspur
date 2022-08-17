from nose.tools import assert_equal
import nose
import convertInspurokl
from configuration import conf_dict
from parse_analy_report import deal_report
from parse_component_log import get_component_info


class TestONEKEYLOG():
    # def test_convertInspurokl_convert(self):
    #     args_input = None
    #     args_path = "C:\question_logs"
    #     args_cpu = None
    #     ret = convertInspurokl.convert(args_input, args_path, args_cpu)
    #     print(ret)

    def testfunc(self):
        a = 2
        b = 2
        assert_equal(a, b)
        print(a == b)

    def test_analy_report(self):
        report_filename = r"C:\question_logs\202111_Tencent_LC21A069000BE_2022-01-08-02-16_ErrorAnalyReport.json"
        rawdata_filename = report_filename.replace("ErrorAnalyReport.json", "RegRawData.json")
        log_filename = report_filename.replace("ErrorAnalyReport.json", "component.log")
        log_cputype_re = conf_dict["log_cputype_re"]
        raw_cputype_re = conf_dict["raw_cputype_re"]
        args_cpu = None
        component_info, error_list1 = get_component_info(log_filename, rawdata_filename, log_cputype_re, raw_cputype_re, args_cpu)
        all_list, error_list = deal_report(report_filename, component_info)
        print("----------------------------")
        print(type(all_list))
        print("----------------------------")
        print(all_list)


if __name__ == "__main__":
    result = nose.run()
    print(result)
    # TestONEKEYLOG.test_convertInspurokl_convert()
    # test = TestONEKEYLOG()
    # test.testfunc()
