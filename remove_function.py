
class remove_expire():

    def __init__(self):			#에러 리포트 와 주소를 받는 함수
    
        #try:
            flag = 0
            #TEXT = DRIVE+str(date.today())+"\ErrorReport"+EXT
            #text = text(TEXT)

            self.folder_removal()
        #except Exception as e:
            #text.write(text.code(e))
            #self.flag = 1

    def remove_readonly(self,func, path, excinfo):  # 지우는 권한을 요청하는 함수
    
        os.chmod(path, stat.S_IWRITE)
        func(path) #overriding the system in the local folders.

    def date_range(self,startDate, endDate):		# 그 사이에 있는 모든 날짜를 상위  함수 에 보고 하는 함수
    
        for n in range(int((endDate-startDate).days)): 
            yield startDate+timedelta(n)

    def calc_3weeks(self,value):				# 오늘 로 부터 3주전의 날짜를 계산 하는 함수
    
        referenceValue = timedelta(days = 21) #21 days
        delta = value-referenceValue;#subtract
        return delta; # checked

    def calc_1year(self,value):					#오늘 로 부터 1년전의 날짜를 계산하는 함수
    
        referenceValue = timedelta(days = 365) #21 days
        delta = value-referenceValue;#subtract
        return delta; # checked

    def folder_removal(self):				# 위 날짜로 부터 각각의 자료들을 없애는 함수
    
            todayDate = date.today()
            # 2. find the 3 weeks before the date
            beforeDate = self.calc_3weeks(todayDate)
            referenceDate = self.calc_1year(beforeDate)
            # 3. within the range from those dates, if and only if they exist
            for i in self.date_range(referenceDate, beforeDate):
                if os.path.isdir(DRIVE+str(i)): #checked
                    #4. remove the file
                   shutil.rmtree(DRIVE+str(i),onerror=self.remove_readonly) #checked.
       

