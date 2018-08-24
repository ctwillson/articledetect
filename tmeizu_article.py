# coding=utf-8
import re
import codecs
import json
#import uniout
def article_check(check_file):
    #pattern = r"([a-zA-Z0-9]+)([\u2E80-\uFFFD]|[\u0030-\u0039]|[\u201c-\u201d]|[\u002d]|[\u003a])"
    #pattern = r"([a-zA-Z0-9][\u4e00-\u9fa5]+)|([\u4e00-\u9fa5][a-zA-Z0-9]+)"
    matcher1 = []
    matcher2 = []
    matcher_dict = {}
    #坑爹的python2
    #pattern = u"([a-zA-Z0-9][\u4e00-\u9fa5]+)|([\u4e00-\u9fa5][a-zA-Z0-9]+)"
    pattern_1 = u"([a-zA-Z0-9]+[\u4e00-\u9fa5])"
    pattern_2 = u"([\u4e00-\u9fa5][a-zA-Z0-9]+)"
    pattern_3 = u"([\d][\u4e00-\u9fa5]+)"
    pattern_4 = u"([\u4e00-\u9fa5][\d]+)"
    pattern1 = re.compile(pattern_1)
    pattern2 = re.compile(pattern_2)
    pattern4 = re.compile(pattern_3)
    pattern5 = re.compile(pattern_4)
    f1 = codecs.open(check_file, 'r', 'utf-8')
    #f1 = open(check_file, 'r', encoding='UTF-8')
    #f1 = open(check_file, 'r')
    count = 0
    #line = f1.read()
    #matcher1 = re.sub(pattern1, line)
    #print (matcher1)
    print u'测试'
    for line in f1.readlines():
        count = count + 1
        #matcher1 = re.sub(pattern1,u"([a-zA-Z0-9]+''[\u4e00-\u9fa5])", line)
        #print matcher1
        matcher1 = re.findall(pattern1, line)
        #matcher1 = ", ".join(matcher1)
        matcher3 = re.findall(pattern2, line)
        #matcher3 = ", ".join(matcher3)
        matcher4 = re.findall(pattern4, line)
        #matcher4 = ", ".join(matcher4)
        matcher5 = re.findall(pattern5, line)
        #matcher5 = ", ".join(matcher5)
  
        #print "matcher3 = ",matcher1,matcher3
        #matcher1 = list(matcher3)
        #matcher1 = json.dumps(matcher1,ensure_ascii=False,encoding="utf8")
        if matcher1 or matcher3 or matcher4 or matcher5:
            matcher_dict[count] = matcher1 + matcher3 + matcher4 + matcher5
            #matcher_dict = json.dumps(matcher_dict, ensure_ascii=False)
            #print matcher_dict 
            #str1 = ''.join(matcher1)
            #matcher1.append(count)
        #    matcher2.append(matcher1)
            #matcher2.append(count)
        #elif matcher3:
        #    matcher2.append(matcher3)
        #elif matcher4:
        #    matcher2.append(matcher4)
        #elif matcher5:
            #matcher2.append(matcher5)
            #matcher2.append(count)
        #if matcher1:
        #    print matcher1
    #print matcher_dict
    #matcher_dict = json.dumps(matcher_dict, ensure_ascii=False)
    print matcher_dict
    #matcher3 = ", ".join(matcher2)
    #f1.close()
    #print "str=",str(matcher2)
    return matcher_dict

if __name__ == '__main__':
    #test1 = unicode(test1,'utf8')
    #p1 = "r'\w[\u2E80-\u9FFF]+'"
    #pattern1 = re.compile(p1)
    #print match1
    #article_check("2017-12-14-teei_daemon-19-04.md")
    #article_check("2017-12-14-teei_daemon-19-04.md")
    article_check("template.md")
