import re
from nltk.tokenize import RegexpTokenizer


class Form():
    # Regex that we need to reference throughout
    fullCourseRegEx = '([A-Z]{2,4}\s[0-9]{3}.[0-9]|[A-Z]{2,4}\s[0-9]{3})'
    courseCodeRegEx = '([A-Z]{2,4})'
    courseNumRegEx = '([0-9]{3}.[0-9]|[0-9]{3})'
    permissionOfInstructor = 'permission\sof\sthe\sinstructor|permission\sfrom\sthe\sinstructor|permission\sof\sthe\sdepartment|by\spermission\sof\sthe\sinstructor|permission of instructor'
    
    def __init__(self, preq:str) -> None:
        self.originalPreq = preq
        self.workingPreq = preq
        self.regCoursePreq = ''
        self.dollarCoursePreq = ''
        self.finalPreq = ''
        self.type = None
        self.formDict = self.createFormDict('Normal_Forms.txt')

    def transformForms(self):
        # Makes things like MATH 176 and 177 -> MATH 176 and MATH 177
        self.formalizeCourseNames()
        # Removes irrelevant statements, replaces symbols/punctuation with appropriate words, and then removes punctuation
        self.removeIrrelevant()
        # Creates string that has $ in place of course codes
        self.replaceCourseCodes()
        # characterizes form (Normal Form, Simple String, Complex String, Normal-Simple)
        self.characterizeForm()
        # create final forms - note, only works for normal forms right now
        self.createFinalForms()
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
        
        # Change MATH 164.3 to MATH 164
        s8 = '([A-Z]{2,4}\s[0-9]{3})\.[0-9]{1,2}'
        s8Replace = '\g<1>'
        
        # Special Case
        s9 = 'Art\s316.6' #Case where they did not put capitals
        s9Replace = 'ART 316'
        s10 = 'SLS240.3'
        s10Replace = 'SLS 240'
        s11 = 'CMPT 481/811'
        s11Replace = 'CMPT 481 or CMPT 811'
        s12 = 'MATH110.3'
        s12Replace = 'MATH 110'
        s13 = 'CMPT146.3'
        s13Replace = 'CMPT 146'
        s14 = 'MUS101.3'
        s14Replace = 'MUS 101'
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
            cur = re.sub(s9, s9Replace, cur)
            cur = re.sub(s10, s10Replace, cur)
            cur = re.sub(s11, s11Replace, cur)
            cur = re.sub(s12, s12Replace, cur)
            cur = re.sub(s13, s13Replace, cur)
            cur = re.sub(s14, s14Replace, cur)
            


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


    def removeIrrelevant(self):
        """Remove irrelevant phrases such as 'or equivalent'. Also replace things like & with 'and'
        
        """
        # Things to remove:
        # (formerly MATH 264)
        # (or equivalent) | or equivalent
        # (taken)
        cur = self.workingPreq
        if cur[0] == ':':
            cur = re.sub(':', '', cur, 1)
        elif cur[0]+cur[1] == '):':
            cur = re.sub('\):', '', cur)
        elif cur[0] == ')':
            cur = re.sub('\)', '', cur, 1)

        s1 = 'formerly\s'+self.fullCourseRegEx+'|formerly\s'+self.courseCodeRegEx
        s2 = 'or equivalents as determined by the college|or\sequivalents|\(or\sequivalent\)|or\sequivalent'
        
        s3 = '\s\(taken\)'
        s4 = 'either\s'+self.fullCourseRegEx+'\sor\s'+self.fullCourseRegEx
        s4Replace = '(\g<1> or \g<2>)'
        s5 = '\&'
        s6 = '3\scredit\sunits\sof|3\scredit\sunits\sfrom'
        s6Replace = 'one of'
        # s7 = ';'
        s8 = '\.'
        s9 = self.fullCourseRegEx+'\sis\srecommended' # ANSC 316.3 is recommended
        s9Replace = '\g<1>'
        s10 = 'some knowledge of macroeconomics preferred'
        s11 = '\('+self.fullCourseRegEx+'\srecommended\)'#(CHEM 115 recommended)
        s12 = self.fullCourseRegEx+'\s\(or\s'+self.fullCourseRegEx+'\)'
        s12Replace = '(\g<1> or \g<2>)'

        cur = re.sub(s1, '', cur)
        cur = re.sub(s2, '', cur)
        cur = re.sub(s3, '', cur)
        cur = re.sub(s4, s4Replace, cur)
        cur = re.sub(s5, 'and', cur)
        cur = re.sub(s6, s6Replace, cur)
        # cur = re.sub(s7, ' and', cur)
        cur = re.sub(s8, '', cur)
        # and/or -> or
        cur = re.sub('and/or', 'or', cur)
        cur = re.sub(s9, s9Replace, cur)
        cur = re.sub(s10, '', cur)
        cur = re.sub('plus', 'and', cur)
        cur = re.sub(s11, '', cur)
        cur = re.sub('at least one of', 'one of', cur)
        cur = re.sub('One of the following courses:', 'One of', cur)
        cur = re.sub('Any one or more of the following courses:', 'One of', cur)
        cur = re.sub('Any one or more of the following courses are recommended as prerequisites for this course:', 'One of', cur)
        cur = re.sub('\(\)', '', cur)
        cur = re.sub('are recommended', '', cur)
        # cur = re.sub(r'Students pursuing the B.Ed. Direct Entry Program must complete', '', cur)
        cur = re.sub(s12, s12Replace, cur)
        cur = re.sub('One course from', 'One of', cur)
        cur = re.sub('[Oo][Rr]', 'or', cur)

        self.workingPreq = cur
        return self.workingPreq
    
    def replaceCourseCodes(self):
        """ replace courses with '$' and permission of instructor with '!'
        """
        mod = self.workingPreq
        if self.workingPreq != 'None':
            # remove punctuation and replace courses with '$'
            # mod = re.sub(r'[^\w\s]', '', mod)
            mod = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', mod)

        mod = re.sub(' {2}', ' ', mod) # remove double spaces
        mod = re.sub(' ,', ',', mod)
        mod = re.sub(' ;', ';', mod)
        mod = re.sub(',,', ',', mod)
        self.dollarCoursePreq = mod.strip()



    def characterizeForm(self):
        
        if self.workingPreq == 'None':
            self.type = 'None'
            return 'None'
        else:
            # remove punctuation and replace courses with '$'
            mod = re.sub(r'[^\w\s]', '', self.workingPreq)
            mod = re.sub('[A-Z]{2,4}\s[0-9]{2,3}.[0-9]|[A-Z]{2,4}\s[0-9]{2,3}', '$', mod)
            # # TESTING - rreplace permission of instrucot/department with ! and count as class essentially
            # mod = re.sub('permission\sof\sthe\sinstructor|permission\sfrom\sthe\sinstructor|permission\sof\sthe\sdepartment|by\spermission\sof\sthe\sinstructor|permission of instructor', '!', mod)
            # list of accepted words for form to be considered 'simple'
            acceptedRegex = '[Aa]nd|[Oo]ne|of|or|\$'
            # formType[0] = Is there a course in the form?
            # formType[1] = Is there a non-normal word in the form?
            formType = [False, False]
            modTokens = mod.split(' ')
            normalStart = []
            for word in modTokens:
                # is the word a course?
                # Want to catch trailing space
                if word != '':
                    # if the word is a course
                    if re.fullmatch('\$', word) != None:
                        formType[0] = True
                        if formType[1] == False:
                            normalStart.append(word)
                    # is the word accepted?
                    elif re.fullmatch(acceptedRegex, word) != None:
                        if formType[1] == False:
                            normalStart.append(word)
                    else:
                        formType[1] = True
                
        
            if formType == [True, True]:
                # print(f'{self.originalPreq}->{self.workingPreq}->{mod}') 
                
                # print(mod)               
                if len(normalStart) == 0:
                    self.type = 'Complex String'
                    # print(f'{self.workingPreq}')
                    # print('\n')
                else:
                    self.type = 'Normal-Simple'
                    # print(f'{self.workingPreq}')
                    # print('\n')
            elif formType == [True, False]:
                # print(f'{self.workingPreq}: {mod}')
                self.type = 'Normal Form'
            elif formType == [False, True]:
                self.type = 'Simple String'
            else:
                self.Type = 'Error'

            return self.type

    def createFinalForms(self):
        if self.type == 'None':
            self.finalPreq = 'None'
            return 'None'
        elif self.type == 'Simple String' or self.type == 'Complex String':
            self.finalPreq = self.workingPreq
            return self.finalPreq
        elif self.type == 'Normal Form':
            # print(f'{self.originalPreq}\n{self.workingPreq}')
            # Create a list of all the classes
            courseList = []
            # remove punctuation before tokenizing
            mod = re.sub(r'[^\w\s]', '', self.workingPreq)
            modTokens = mod.split(' ')
            for j in range(len(modTokens)-1):
                word = modTokens[j]+' '+modTokens[j+1]
                if re.fullmatch(self.fullCourseRegEx, word) != None:
                    courseList.append(word)
            # print(f'{self.originalPreq}\n{self.workingPreq}\n')
            # find matching finalForm
            finalForm = self.formDict[self.dollarCoursePreq]
            if finalForm == None:
                # print('Error: no matching input for:'+self.dollarCoursePreq)
                return ''
            
            # one by one replace $ with a course from courseList
            # print(courseList)
            for j in range(len(courseList)):
                finalForm = re.sub('\$', courseList[j], finalForm, 1)


            self.finalPreq = finalForm.rstrip()
            return finalForm.rstrip()

        elif self.type == 'Normal-Simple':
            # print(f'{self.originalPreq}\n{self.workingPreq}\n{self.dollarCoursePreq}')
            # need to seperate first part of string from second part of string
            # then treat second part of string as a class
            # then do same thing as in normal forms
            courseList = []
            remainingStr = ''
            # remove punctuation before tokenizing
            mod = re.sub(r'[^\w\s]', '', self.workingPreq)
            modTokens = mod.split(' ')
            for j in range(len(modTokens)-1):
                word = modTokens[j]+' '+modTokens[j+1]
                if re.fullmatch(self.fullCourseRegEx, word) != None:
                    courseList.append(word)
            acceptedRegex = '[Aa]nd.{0,1}|[Oo]ne.{0,1}|of.{0,1}|or.{0,1}|\$.{0,1}\W{0,1}'
            # mod = re.sub(r'[^\w\s]', '', self.workingPreq)
            mod = self.dollarCoursePreq.split(' ')
            reached = False
            for j in range(1, len(mod)):

                check = re.sub(r'[^\w\s]', '', mod[j])
                if re.fullmatch(acceptedRegex, mod[j]) == None and not reached:
                    # add remaining string as if it were a course
                    # courseList.append(' '.join(mod[j:]))
                    remainingStr = ' '.join(mod[j:])
                    # make dollarCoursePreq represent that
                    newDollarList = mod[:j]
                    newDollarList.append('$')
                    self.dollarCoursePreq = ' '.join(newDollarList)
                    reached = True

            # find matching finalForm
            finalForm = self.formDict[self.dollarCoursePreq]
            # we want to replace final dollar sign with remaining string
            reverse = finalForm[::-1]
            remainingReverse = remainingStr[::-1]
            reverse = re.sub('\$', remainingReverse, reverse, 1)
            finalForm = reverse[::-1]
            # replace $ with course names
            for j in range(len(courseList)):
                finalForm = re.sub('\$', courseList[j], finalForm, 1)

            self.finalPreq = finalForm.rstrip()
            # print(f'{finalForm}\n')
            return finalForm.rstrip()
         
        
        return ''

    def createFormDict(self, filename):
        formDict = {}
        f = open(filename, 'r')
        lines = f.readlines()
        for line in lines:
            inputForm = line.split('\t')[0]
            outputForm = line.split('\t')[1]
            formDict[inputForm] = outputForm
        
        return formDict


            
        






            
