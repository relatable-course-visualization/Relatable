import re
from nltk.tokenize import RegexpTokenizer


class Form():
    # Regex that we need to reference throughout
    fullCourseRegEx = '([A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3})'
    courseCodeRegEx = '([A-Z]{2,4})'
    courseNumRegEx = '([0-9]{2,3}.[0-9]|[0-9]{2,3})'

    def __init__(self, preq:str) -> None:
        self.originalPreq = preq
        self.workingPreq = preq
        self.finalPreq = ''
        self.type = None

    def transformForms(self):
        self.formalizeCourseNames()
        self.removeIrrelevant()
        return self.workingPreq
    
    def formalizeCourseNames(self):
        """ Replace occurances of implicit course codes with explicit course codes
            PostCond: self.workingPreq will be modified;
                      Occurances like CMPT 141 and 145 will become CMPT 141 and CMPT 145
        """
        # Regular expressions we want to catch:
        #1. ex: CMPT 141 and 145
        s1 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+',*\sand\s'+self.courseNumRegEx 
        s1Replace = '\g<1> \g<2> and \g<1> \g<3>'
        #2. ex: CMPT 141 or 145
        s2 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+'\s,*or\s'+self.courseNumRegEx 
        s2Replace = '\g<1> \g<2> or \g<1> \g<3>'
        #3. ex: CMPT 140, 145
        s3 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+',*\s'+self.courseNumRegEx 
        s3Replace = '\g<1> \g<2>, \g<1> \g<3>' 
        #4. ex: CMPT 141 and (145 or 150)
        s4 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+'\sand\s('+self.courseNumRegEx+'\sor\s'+self.courseNumRegEx+')' 
        s4Replace = '\g<1> \g<2> and (\g<1> \g<3> or \g<1> \g<4>)'
        #5. ex: CMPT 141 (or 116)
        s5 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+'\s\(or\s'+self.courseNumRegEx+'\)' 
        s5Replace = '\g<1> \g<2> or \g<1> \g<3>'
        #6. ex: CMPT 110 & 116
        s6 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+'\s\&\s'+self.courseNumRegEx 
        s6Replace = '\g<1> \g<2> and \g<1> \g<3>'
        #7. ex: SOC 212 and (234 or 329).
        s7 = self.courseCodeRegEx+'\s'+self.courseNumRegEx+'\sand\s\('+self.courseNumRegEx+'\sor\s'+self.courseNumRegEx
        s7Replace = '\g<1> \g<2> and (\g<1> \g<3> or \g<1> \g<4>'
        # Special Case
        s8 = 'Art\s316.6' #Case where they did not put capitals
        s8Replace = 'ART 316'


        # Note - from testing this catches all cases that occur - will have to test after each new cycle

        # Now, one by one we want to perform replacements:
        prev = self.workingPreq
        cur = self.workingPreq
        while True:
            cur = re.sub(s1, s1Replace, cur)
            cur = re.sub(s2, s2Replace, cur)
            cur = re.sub(s3, s3Replace, cur)
            cur = re.sub(s4, s4Replace, cur)
            cur = re.sub(s5, s5Replace, cur)
            cur = re.sub(s6, s6Replace, cur)
            cur = re.sub(s7, s7Replace, cur)
            cur = re.sub(s8, s8Replace, cur)
            if cur == prev:
                # print(f'{prev} : {cur}')
                break       
            else:
                # print(prev)
                # print(cur)
                # print('\n')
                prev = cur

        # self.workingPreq = re.sub(s8, s8Replace, self.workingPreq)
        self.workingPreq = cur
        return self.workingPreq

    def identifyForms(self):
        """Identifies all possible logical forms and seperates them from strings
        """
        # Need to tokenize and then analyze collection of strings
        # seperate into sections splitting on 'or', 'and', 'and one of', ';'
        # this will give us smaller and simpler strings to analyize

    def removeIrrelevant(self):
        """Remove irrelevant phrases such as 'or equivalent'. Also replace things like & with 'and'
        
        """
        # Things to remove:
        # (formerly MATH 264)
        # (or equivalent) | or equivalent
        # (taken)
        cur = self.workingPreq
        s1 = '\(formerly\s'+self.courseCodeRegEx+'\)'
        s2 = '\(or\sequivalent\s\)|or\sequivalent'
        s3 = '\(taken\)'
        # s4 = '\.' Math 166.3
        s5 = '\&'


        cur = re.sub(s1, '', cur)
        cur = re.sub(s2, '', cur)
        cur = re.sub(s3, '', cur)
        # cur = re.sub(s4, '', cur)
        cur = re.sub(s5, 'and', cur)

        self.workingPreq = cur
        return self.workingPreq
    
    def characterizeForm(self):
        if self.workingPreq == 'None':
            self.type = 'None'
            return 'None'
        else:
            # remove punctuation and replace courses with '$'
            mod = re.sub(r'[^\w\s]', '', self.workingPreq)
            mod = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', mod)
            # # TESTING - rreplace permission of instrucot/department with ! and count as class essentially
            mod = re.sub('permission\sof\sthe\sinstructor|permission\sfrom\sthe\sinstructor|permission\sof\sthe\sdepartment|by\spermission\sof\sthe\sinstructor', '!', mod)
            # list of accepted words for form to be considered 'simple'
            acceptedRegex = '[Aa]nd|[Oo]ne|of|or|\$|!'
            # formType[0] = Is there a course in the form?
            # formType[1] = Is there a non-normal word in the form?
            formType = [False, False]
            modTokens = mod.split(' ')
            normalStart = []
            for word in modTokens:
                # is the word a course?
                # Want to catch trailing space
                if word != '':
                    if re.search('\$', word) != None:
                        formType[0] = True
                        if formType[1] == False:
                            normalStart.append(word)
                    # is the word accepted?
                    elif re.search(acceptedRegex, word) != None:
                        if formType[1] == False:
                            normalStart.append(word)
                    else:
                        formType[1] = True
                
            
            if formType == [True, True]:
                # print(f'{self.originalPreq}->{self.workingPreq}->{mod}') 
                
                # print(mod)               
                if len(normalStart) == 0:
                    self.type = 'Complex String'
                    print(self.workingPreq)
                    print('\n')
                else:
                    self.type = 'Normal-Simple'
            elif formType == [True, False]:
                # print(f'{self.workingPreq}: {mod}')
                self.type = 'Normal Form'
            elif formType == [False, True]:
                self.type = 'Simple String'
            else:
                self.Type = 'Error'

            return self.type

    def characterizeComplex(self):
        """ Given a form that is characterized as complex, is it possible to split it into two parts:
            a normal form and a simple form
        """
        if self.type != 'Complex Form':
            return False
        






            
