import os
import os.path
import shutil
import json
import sys
import sys.argv



sys_argv_1 = ''
sys_argv_2 = ''
sys_argv_3 = ''
sys_argv_4 = ''
sys_argv_5 = ''

def CallError(ScriptName):
    pass

def read_comand(dataofcomandlocal):
    global sys_argv_1
    global sys_argv_2
    global sys_argv_3
    global sys_argv_4
    global sys_argv_5
    sys_argv_1 = dataofcomandlocal['sys_argv_1']
    sys_argv_2 = dataofcomandlocal['sys_argv_2']
    sys_argv_3 = dataofcomandlocal['sys_argv_3']
    sys_argv_4 = dataofcomandlocal['sys_argv_4']
    sys_argv_5 = dataofcomandlocal['sys_argv_5']

def DoResponse(response_filename,str):
    temp_name = response_filename + "_temp"
    if os.path.exists(temp_name):
        os.remove(temp_name)
    data = {}  
    data['Response'] = str
    with open(temp_name, 'w') as outfile:
        json.dump(data, outfile)
    if os.path.exists(response_filename):
        os.remove(response_filename)
    shutil.move(temp_name, response_filename)
    #oldfile = io.File(response_filename)
    #oldfile.renameTo(response_filename)
    #os.rename(response_filename, response_filename)
    #logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    #logging.debug(response_filename)



def AtomIsOpen():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/AtomIsOpen.sikuli/1463230028949.png").similar(0.80)):
        exit(1)    
    
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/AtomIsOpen.sikuli/1463230028949.png").similar(0.80).targetOffset(10,0))
    
    type("n",KeyModifier.CTRL)
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/AtomIsOpen.sikuli/Edit.png")
    wait("C:/Commons/rep/vanessa-automation/tools/Sikuli/AtomIsOpen.sikuli/SelectGramma.png",30)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/AtomIsOpen.sikuli/SelectGramma.png")
    
    sleep(2)
    paste("Gherkin-ru")
    sleep(1)
    type(Key.ENTER)
    pass

def CallQueryConstructWithResult():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/Texcr.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/Texcr.png")
    else:
        exit(1)
        
    sleep(1)
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/OIlCTDplTODS.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/OIlCTDplTODS.png")
    else:
        exit(1)
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/1474556643856.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CallQueryConstructWithResult.sikuli/1474556643856.png")
    else:
        exit(1)
    
    
    pass

def ChooseGherkin():
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ChooseGherkin.sikuli/O6ununi.png").similar(0.60),15):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ChooseGherkin.sikuli/O6ununi.png").similar(0.60))
    else:
        exit(1)
        
    sleep(1)    
    
    pass

def ClickButtonDobavit():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonDobavit.sikuli/HOBBBVITI.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonDobavit.sikuli/HOBBBVITI.png")
    sleep(1)
    pass

def ClickButtonLoadFeatures():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonLoadFeatures.sikuli/Sarnvzsm.png")
    sleep(1.5)
    #click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonLoadFeatures.sikuli/EIlD3HTbUHHH.png")
    #sleep(1.5)
    pass

def ClickButtonProvestiIZakrit():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonProvestiIZakrit.sikuli/np0BCTMM36Kp.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonProvestiIZakrit.sikuli/np0BCTMM36Kp.png")
    sleep(1)
    pass

def ClickButtonSozdat():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonSozdat.sikuli/Coagarb.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickButtonSozdat.sikuli/Coagarb.png")
    sleep(1)
    pass

def ClickContextMenuOpenFeatureInTextEditor():
    hover("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickContextMenuOpenFeatureInTextEditor.sikuli/1532879519618.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickContextMenuOpenFeatureInTextEditor.sikuli/1532879519618.png")
    pass

def ClickContextMenuVisualStudioCode():
    hover("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickContextMenuVisualStudioCode.sikuli/1532879285882.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickContextMenuVisualStudioCode.sikuli/1532879285882.png")
    pass

def ClickCoordinates():
    location = Location(int(sys_argv_1),int(sys_argv_2))
    click(location)
    
    
    #findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickCoordinates.sikuli/1492761928555.png")
    #mm = SCREEN.getLastMatches()
    #while mm.hasNext(): # loop as long there is a first and more matches
    #    TekMatch = mm.next()
    #    print "found: ", TekMatch   # access the next match in the row
    #    location = TekMatch.getTarget()
    #    print "match",";",location.x,";",location.y
    #    click(location)
    #    sleep(1)
    #    print mm.x
    #    t1= capture(mm.getX(), mm.getY(), mm.getW(), mm.getH())

def ClickFieldSkladPrihNakl():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFieldSkladPrihNakl.sikuli/Cmap.png"):
        exit(1)
        
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFieldSkladPrihNakl.sikuli/Cmap.png").targetOffset(39,1))
    sleep(1)
    pass

def ClickFlagGenUF():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFlagGenUF.sikuli/_H9DMDOB8TbV.png").targetOffset(-131,0)):
        exit(1)
        
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFlagGenUF.sikuli/_H9DMDOB8TbV.png").targetOffset(-131,0))
    sleep(1)
    pass

def ClickFlagMakeOblast():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFlagMakeOblast.sikuli/C03AEBSTbOSI.png").targetOffset(-143,1)):
        exit(1)
        
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickFlagMakeOblast.sikuli/C03AEBSTbOSI.png").targetOffset(-143,1))
    sleep(1)
    pass

def ClickGeneratorEPF():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickGeneratorEPF.sikuli/FenepampEPF.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickGeneratorEPF.sikuli/FenepampEPF.png")
    sleep(1)
    pass

def ClickMenuPrihNakl():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickMenuPrihNakl.sikuli/HQHXOLLHBHH3.png").similar(0.50)):
        exit(1)
        
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickMenuPrihNakl.sikuli/HQHXOLLHBHH3.png").similar(0.50))
    sleep(1)
    pass

def ClickOnPicture():
    PictureToClick = sys_argv_1
    
    Find = 0
    if Find == 0:
        if exists(Pattern(PictureToClick).similar(0.70)):
            click(Pattern(PictureToClick).similar(0.70))
            Find = 1
    
    if Find == 0:
        if exists(Pattern(PictureToClick).similar(0.60)):
            click(Pattern(PictureToClick).similar(0.60))
            Find = 1
    
    if Find == 0:		
        click(Pattern(PictureToClick).similar(0.50))
    
    pass
    	

def ClickRazdelOsnovnaya():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickRazdelOsnovnaya.sikuli/Ocnozmasa.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickRazdelOsnovnaya.sikuli/Ocnozmasa.png")
    sleep(1)
    pass

def ClickRightOnPicture():
    PictureToClick = sys_argv_1
    rightClick(PictureToClick)
    pass

def ClickSaveFF():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickSaveFF.sikuli/nvnmamrrrhaf.png",15):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickSaveFF.sikuli/nvnmamrrrhaf.png")
        pass
    exit(1)

def ClickServiceTab():
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickServiceTab.sikuli/Cepsuc.png")
    pass

def ClickTabScenariyPovedeniya():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickTabScenariyPovedeniya.sikuli/AEITOMGTMSMD.png"):
        exit(1)
        
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickTabScenariyPovedeniya.sikuli/AEITOMGTMSMD.png").targetOffset(-31,33))
    sleep(1)
    pass

def ClickToVspomogatelnayaTab():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickToVspomogatelnayaTab.sikuli/1538754420263.png")

def ClickUITab():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickUITab.sikuli/Pa60TacUI.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickUITab.sikuli/Pa60TacUI.png")
    sleep(1)
    pass

def ClickWordScenario():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickWordScenario.sikuli/1475226909136.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ClickWordScenario.sikuli/1475226909136.png")
    sleep(1)
    pass

def CloseConfigurator():
    type(Key.F4, KeyModifier.ALT)
    sleep(1)
    pass

def CloseMPC():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseMPC.sikuli/1579760357923.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseMPC.sikuli/1579760357923.png")
        sleep(1)
        type("x", KeyModifier.ALT)
        
    pass    
        

def CloseNotePadPlusPlus():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseNotePadPlusPlus.sikuli/1579791874165.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseNotePadPlusPlus.sikuli/1579791874165.png")
        sleep(1)
        type(Key.F4, KeyModifier.ALT)
        pass
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseNotePadPlusPlus.sikuli/1579791681384.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseNotePadPlusPlus.sikuli/1579791681384.png")
        sleep(1)
        type(Key.F4, KeyModifier.ALT)
        pass
        
    pass    
        

def CloseProgrammsAfterTests():
    #if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1575100124038.png"):
    #    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1575100124038.png").targetOffset(-40,-1))
    #    sleep(3)
    
    
    #if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1575100176851.png"):
    #    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1575100176851.png").targetOffset(-39,-2))
    #    sleep(3)
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572346966410.png")
        sleep(3)
    
        
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png").targetOffset(-18,-1))
        sleep(5)
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png").targetOffset(-18,-1))
        sleep(5)
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png").targetOffset(-18,-1))
        sleep(5)
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseProgrammsAfterTests.sikuli/1572347071932.png").targetOffset(-18,-1))
        sleep(5)

def CloseWinExplorer():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseWinExplorer.sikuli/1579792079784.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseWinExplorer.sikuli/1579792079784.png").targetOffset(4,15))
        sleep(1)
        type(Key.F4, KeyModifier.ALT)
        pass
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseWinExplorer.sikuli/1596467122234.png"):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CloseWinExplorer.sikuli/1596467122234.png").targetOffset(1,13))
        sleep(1)
        type(Key.F4, KeyModifier.ALT)
        pass
    
    
    
        
    pass    
        

def CollapseServiceArea():
    Found = 0
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CollapseServiceArea.sikuli/06narwbCJryx.png").targetOffset(-159,0)):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CollapseServiceArea.sikuli/06narwbCJryx.png").targetOffset(-159,0))
        Found = 1
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CollapseServiceArea.sikuli/O5JIBCIZbCr1.png").targetOffset(-194,-2)):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/CollapseServiceArea.sikuli/O5JIBCIZbCr1.png").targetOffset(-194,-2))
        Found = 1
    
    if Found == 0:
        exit(1)
        
    sleep(1)
    pass
    

def ConfiguratorIsOpen():
    kol = 0
    while True:
        if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ConfiguratorIsOpen.sikuli/DrnaxmaAumuu.png").similar(0.60),5):
            break
        FindIm = findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/ConfiguratorIsOpen.sikuli/1464643667457.png") 
        ArrOfImage = list(FindIm)
        KolImages  = len(ArrOfImage)
        print 'KolImages='+ str(KolImages)
        for n in range(0, KolImages):
            t = ArrOfImage[n]
            print 't.x='+ str(t.x)
        if KolImages > 0:
            t = ArrOfImage[KolImages-1]
            print 'click t.x='+ str(t.x)
            click(Location(t.x+5,t.y+5))
            #click(t1)
            #click(ArrOfImage[KolImages-1])
        sleep(1)
        kol = kol+1
        if kol > 5:
            exit(1)
    
    pass

def ContextMenu():
    type(Key.F10, KEY_SHIFT)
    pass

def CtrlC():
    type('c', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlF():
    type('f', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlH():
    type('h', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlN():
    type('n', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlO():
    type('o', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlPlus():
    type(Key.ADD,KeyModifier.CTRL)
    sleep(0.5)
    pass

def CtrlS():
    type('s', KeyModifier.CTRL)
    sleep(1)
    pass

def CtrlV():
    type('v', KeyModifier.CTRL)
    sleep(1)
    pass

def DeleteLineWithText():
    path2file = sys_argv_1
    file = open(path2file, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        stroka = unicode(line, 'utf-8')
        type('f', KeyModifier.CTRL)
        sleep(1)
        paste(stroka)
        sleep(1)
        type(Key.ENTER)
        sleep(1)
        type(Key.ESC)
        sleep(1)
        type(Key.HOME)
        type(Key.HOME)
        sleep(1)
        type('l', KeyModifier.CTRL)
        break
    
    pass

def DoAltF4():
    type(Key.F4, KeyModifier.ALT)
    sleep(1)
    pass

def DoCtrlF4():
    type(Key.F4, KeyModifier.CTRL)
    sleep(1)
    pass

def DoReplace():
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/DoReplace.sikuli/Bameumbrace.png").similar(0.80))
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/DoReplace.sikuli/3abnb.png")
    pass

def DoubleClickOnPicture():
    PictureToClick = sys_argv_1
    doubleClick(PictureToClick)
    pass

def DragAndDrop():
    PictureToClick1 = sys_argv_1
    PictureToClick2 = sys_argv_2
    dragDrop(PictureToClick1,PictureToClick2)
    pass

def Exit1C():
    type(Key.F4, KeyModifier.ALT)
    pass

def FeatureLoadMany():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/FeatureLoadMany.sikuli/Sarnvzsm.png")
    sleep(1.5)
    hover("C:/Commons/rep/vanessa-automation/tools/Sikuli/FeatureLoadMany.sikuli/iarpvambqmai.png")
    sleep(1.5)
    pass

def FeatureLoadOne():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/FeatureLoadOne.sikuli/Sarnvzsm.png")
    sleep(1)
    hover("C:/Commons/rep/vanessa-automation/tools/Sikuli/FeatureLoadOne.sikuli/EIlD3HTbUHHH.png")
    sleep(1)
    pass

def FirstFeature():
    # Посимвольный вывод символов
    def VyvestiStrokuPosimvolno(stroka):
        dlina = len(stroka)
        i = 0
        while i < dlina:
            tekSimvol = stroka[i]
            paste(tekSimvol)
            sleep(0.05)
            i = i + 1
    
    # Паузы
    ShortBreak = 1
    MiddleBreak = 3
    BigBreak = 5
    
    step = sys_argv_1
    
    # Открытие текстового редактора
    if step == "1":
        type('r', KeyModifier.WIN)
        type(Key.DELETE)
        sleep(ShortBreak)
    #    paste(u"notepad++ -nosession")
        paste(u"atom")
        sleep(MiddleBreak)
        type(Key.ENTER)
        sleep(MiddleBreak)
        pass
    # Ввод текста
    elif step == "2":
        #type('n', KeyModifier.CTRL)
        path2file = sys_argv_2
        file = open(path2file, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            stroka = unicode(line, 'utf-8')
            VyvestiStrokuPosimvolno(stroka)
        sleep(BigBreak)
        pass
    # Сохранение текста
    elif step == "3":
        path2VanessaBehavoirFeature = sys_argv_2
        type('s', KeyModifier.CTRL)
        sleep(1)
        type(Key.DELETE)
        sleep(1)
        paste(path2VanessaBehavoirFeature)
        pass
    elif step == "4":
        type(Key.ENTER)
        type(Key.F4, KeyModifier.ALT)
        sleep(BigBreak)
        pass
        

def GenerateEPF():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/GenerateEPF.sikuli/C0a11aTbM061.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GenerateEPF.sikuli/C0a11aTbM061.png")
    sleep(1)
    pass

def GetAll1CWindowsCoordinates():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetAll1CWindowsCoordinates.sikuli/1492761928555.png"):
        findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetAll1CWindowsCoordinates.sikuli/1492761928555.png")
    elif exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetAll1CWindowsCoordinates.sikuli/1543849229768.png"):
        findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetAll1CWindowsCoordinates.sikuli/1543849229768.png")
    
        
    mm = SCREEN.getLastMatches()
    while mm.hasNext(): # loop as long there is a first and more matches
        TekMatch = mm.next()
    #    print "found: ", TekMatch   # access the next match in the row
        location = TekMatch.getTarget()
        print "match",";",location.x,";",location.y
    #    click(location)
    #    sleep(1)
    #    print mm.x
    #    t1= capture(mm.getX(), mm.getY(), mm.getW(), mm.getH())

def GetDebuggerUrl():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580195036155.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580195036155.png")
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580196313479.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580196313479.png")
        
        
    
    wait("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139116047.png",60)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139135270.png")
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139153268.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139167834.png")
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139216233.png").targetOffset(12,23))
    
    sleep(1)
    
    type("c", KeyModifier.CTRL)
    
    sleep(1)
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139310601.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetDebuggerUrl.sikuli/1580139330423.png")
    
    
    Clipboard = App.getClipboard();
    
    FileName = sys_argv_1
    #FileName = "C:/Temp/111.txt"
    
    text = Clipboard
    f = open(FileName, 'w')
    
    f.write(text)
    f.flush()
    f.close()
    
    pass

def GetPictureCoordinats():
    import json
    
    PictureToFind = sys_argv_1
    temp_name = sys_argv_2
    
    Find = 0
    
    if Find == 0:
        if exists(Pattern(PictureToFind).similar(0.70)):
            match = find(Pattern(PictureToFind).similar(0.70))
    	    Find = 1
    	
    if Find == 0:
        if exists(Pattern(PictureToFind).similar(0.60)):
            match = find(Pattern(PictureToFind).similar(0.60))
    	    Find = 1
    
    if Find == 0:
        match = find(Pattern(PictureToFind).similar(0.50))
    
    #temp_name = 'c:/temp/111.json'
    #match = find("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetPictureCoordinats.sikuli/1547221183087.png")
    
    data = {} 
    data['X1'] = match.getTopLeft().x
    data['Y1'] = match.getTopLeft().y
    data['X2'] = match.getBottomRight().x
    data['Y2'] = match.getBottomRight().y
    
    with open(temp_name, 'w') as outfile:
        json.dump(data, outfile)
    	
    pass    
    #print ("X="+str(match.x))

def GetVideoClickDownload():
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GetVideoClickDownload.sikuli/JnCncauannvm.png")
    sleep(1)
    pass

def Git():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/Git.sikuli/Nmc.png",15):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/Git.sikuli/Nmc.png")
        pass
    exit(1)

def GoToEndOfLineWithShift():
    if Env.isLockOn(Key.NUM_LOCK):
        nlZap=True
    else:
        nlZap=False
    if nlZap: type(Key.NUM_LOCK)
    
    keyDown(Key.SHIFT)
    sleep(0.5)
    
    type(Key.END)
    sleep(0.5)
    keyUp()
    
    if nlZap: type(Key.NUM_LOCK)
    
    pass

def GoToEndOfModule():
    type(Key.END,KeyModifier.CTRL)
    sleep(0.5)
    type(Key.ENTER)
    sleep(0.5)
    pass

def GoToFormModule():
    FindIm = findAll(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/GoToFormModule.sikuli/EIMoaunb.png").similar(0.50)) 
    ArrOfImage = list(FindIm)
    KolImages  = len(ArrOfImage)
    if KolImages == 0:
        exit(1)
    t = ArrOfImage[0]
    click(Location(t.x+5,t.y+5))
    sleep(1)
    pass

def GoToProcedure():
    path2file = sys_argv_1
    file = open(path2file, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        stroka = unicode(line, 'utf-8')
        type('f', KeyModifier.CTRL)
        sleep(1)
        paste(stroka)
        sleep(1)
        type(Key.ENTER)
        sleep(1)
        break
    
    pass

def GoToTabScenarioRun():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GoToTabScenarioRun.sikuli/1532879384495.png")
    pass

def GoToTabService():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/GoToTabService.sikuli/1532878657983.png")
    pass

def HotKey():
    HotKey = sys_argv_1
    Modif = sys_argv_2 
    
    lowerHotKey = str.lower(HotKey.encode('utf-8'))
    if lowerHotKey == 'f1':
        HotKey = Key.F1
    elif lowerHotKey == 'f2':
        HotKey = Key.F2
    elif lowerHotKey == 'f3':
        HotKey = Key.F3
    elif lowerHotKey == 'f4':
        HotKey = Key.F4
    elif lowerHotKey == 'f5':
        HotKey = Key.F5
    elif lowerHotKey == 'f6':
        HotKey = Key.F6
    elif lowerHotKey == 'f7':
        HotKey = Key.F7
    elif lowerHotKey == 'f8':
        HotKey = Key.F8
    elif lowerHotKey == 'f9':
        HotKey = Key.F9
    elif lowerHotKey == 'f10':
        HotKey = Key.F10
    elif lowerHotKey == 'f11':
        HotKey = Key.F11
    elif lowerHotKey == 'f12':
        HotKey = Key.F12
    elif lowerHotKey == 'del':
        HotKey = Key.DELETE
    elif lowerHotKey == 'delete':
        HotKey = Key.DELETE
    elif lowerHotKey == 'left':
        HotKey = Key.LEFT
    elif lowerHotKey == 'right':
        HotKey = Key.RIGHT
    elif lowerHotKey == 'up':
        HotKey = Key.UP
    elif lowerHotKey == 'down':
        HotKey = Key.DOWN
    elif lowerHotKey == 'esc':
        HotKey = Key.ESC
    elif lowerHotKey == 'end':
        HotKey = Key.END
    elif lowerHotKey == 'home':
        HotKey = Key.HOME
    elif lowerHotKey == 'tab':
        HotKey = Key.TAB
    
    if Modif == 'win':
        type(HotKey, KeyModifier.WIN)
    elif Modif == 'ctrl':
        type(HotKey, KeyModifier.CTRL)
    elif Modif == 'alt':
        type(HotKey, KeyModifier.ALT)
    elif Modif == 'shift':
        type(HotKey, KeyModifier.SHIFT)
    elif Modif == 'no':
        type(HotKey)
    else:
        print "wrong modifikator: " + Modif
        exit(1)
    
    pass    

def IGoToConditions():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToConditions.sikuli/Vrnnnvm.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToConditions.sikuli/Vrnnnvm.png")
    else:
        exit(1)
        
    pass

def IGoToLeftSideOfConditions():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToLeftSideOfConditions.sikuli/Hons.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToLeftSideOfConditions.sikuli/Hons.png")
    else:
        exit(1)
        
    pass

def IGoToTablesAndFields():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToTablesAndFields.sikuli/Ta6nvnu1vann.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/IGoToTablesAndFields.sikuli/Ta6nvnu1vann.png")
    else:
        exit(1)
        
    pass

def IPressOkInQueryConstruct():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/IPressOkInQueryConstruct.sikuli/OK-1.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/IPressOkInQueryConstruct.sikuli/OK-1.png")
    else:
        exit(1)
        
    pass

def LoadingFeatureFileInBehavior():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/LoadingFeatureFileInBehavior.sikuli/J93ar.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/LoadingFeatureFileInBehavior.sikuli/Barpysvm0Auy.png")
    sleep(1)
    path2FeatureFile = sys_argv_1
    paste(path2FeatureFile)
    sleep(3)
    type(Key.ENTER)
    pass

def MoveActiveWindowFullScreen():
    type(Key.UP, KeyModifier.WIN)
    sleep(1)
    pass

def MoveActiveWindowLeft():
    type(Key.LEFT, KeyModifier.WIN)
    sleep(1)
    pass

def MoveActiveWindowRight():
    type(Key.RIGHT, KeyModifier.WIN)
    sleep(1)
    pass

def MoveMouseToPicture():
    PictureToClick = sys_argv_1
    
    Find = 0
    if Find == 0:
        if exists(Pattern(PictureToClick).similar(0.70)):
            hover(Pattern(PictureToClick).similar(0.70))
            Find = 1
    
    
    if Find == 0:
        if exists(Pattern(PictureToClick).similar(0.60)):
            hover(Pattern(PictureToClick).similar(0.60))
            Find = 1
    
    
    if Find == 0:
        if exists(Pattern(PictureToClick).similar(0.50)):
            hover(Pattern(PictureToClick).similar(0.50))
            Find = 1
    
    
    pass

def NotePadIsOpen():
    exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/NotePadIsOpen.sikuli/FIBW.png")
    pass

def OpenBehavior():
    sleep(5)
    type('o', KeyModifier.CTRL)
    sleep(1)
    path2VanessaBehavoir = sys_argv_1
    paste(path2VanessaBehavoir)
    sleep(2)
    type(Key.ENTER)
    pass

def OpenDialog():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialog.sikuli/1462546926131.png")
    sleep(0.5)
    type(Key.DOWN)
    sleep(0.5)
    type(Key.RIGHT)
    sleep(0.5)
    type(Key.DOWN)
    sleep(0.5)
    #type(Key.ENTER)
    #sleep(1)
    pass

def OpenDialogClick():
    #if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogClick.sikuli/Flmnduana.png").targetOffset(34,0)):
    #    exit(1)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogClick.sikuli/Flmnduana.png").targetOffset(34,0))
    pass

def OpenDialogClickFolder():
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogClickFolder.sikuli/Ilama.png").targetOffset(23,0))
    pass

def OpenDialogClickFolderSelect():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogClickFolderSelect.sikuli/Bb60pnanxm.png")
    pass

def OpenDialogConf():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogConf.sikuli/in.png").similar(0.60)):
        exit(1)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenDialogConf.sikuli/in.png").similar(0.60))
    sleep(0.5)
    pass

def OpenFeatureFileInRedactor():
    rightClick(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenFeatureFileInRedactor.sikuli/1463774011187.png").similar(0.60))
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenFeatureFileInRedactor.sikuli/TIDbTbmature.png")
    sleep(1)
    pass

def OpenFile():
    path = sys_argv_1
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenFile.sikuli/MdaainaHIFIH.png").targetOffset(36,0))
    sleep(1)
    paste(path )
    sleep(1)
    type(Key.ENTER)
    pass
    

def OpenMainFormOfEPF():
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenMainFormOfEPF.sikuli/___xQI.png").similar(0.60)):
        exit(1)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenMainFormOfEPF.sikuli/___xQI.png").similar(0.60).targetOffset(16,0))
    sleep(1)
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenMainFormOfEPF.sikuli/Pupma.png"):
        doubleClick("C:/Commons/rep/vanessa-automation/tools/Sikuli/OpenMainFormOfEPF.sikuli/Pupma.png")
        
    pass

def PictExists():
    import json
    
    PictureToFind = sys_argv_1
    res = 0
    if exists(Pattern(PictureToFind).similar(0.60)):
        res = 1
        
    temp_name = sys_argv_2
    
    #temp_name = 'c:/temp/111.json'
    #match = find("C:/Commons/rep/vanessa-automation/tools/Sikuli/PictExists.sikuli/1547221183087.png")
    
    data = {} 
    data['exists'] = res
    
    with open(temp_name, 'w') as outfile:
        json.dump(data, outfile)
    pass    
    #print ("X="+str(match.x))

def PressEnd():
    type(Key.END)
    sleep(1)
    pass

def PressEndEnter():
    type(Key.END)
    type(Key.ENTER)
    sleep(0.5)
    pass

def PressTab():
    type(Key.TAB)
    pass

def Python():
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/Python.sikuli/won3.png").similar(0.89),15):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/Python.sikuli/won3.png").similar(0.89))
        pass
    exit(1)

def ReloadScenarios():
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/ReloadScenarios.sikuli/_9D938IDV3HT.png")
    sleep(1.5)
    pass

def RunScenarios():
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/RunScenarios.sikuli/BbHDJlHHTbCL.png").similar(0.80))
    sleep(1.5)
    pass

def SaveChangesCtrls():
    type('s', KeyModifier.CTRL)
    sleep(1)
    pass

def SaveZamer():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198185757.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198185757.png")
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198209410.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198209410.png")
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198233333.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198252352.png")
    
    sleep(1)
    
    type("a", KeyModifier.CTRL)    
    
    sleep(1)
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198301825.png")
    
    sleep(3)
    
    Path = sys_argv_1
    #Path = "C:\Commons\Zamer\pff\UF"
    
    App.setClipboard(Path)
    
    sleep(1)
    
    type("v", KeyModifier.CTRL)
    
    sleep(1)
    
    type(Key.ENTER)
    
    sleep(1)
    
    while True:
       if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198667799.png"):
           click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198667799.png")
           sleep(3)
       else:
           break
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198803823.png")
    
    sleep(1)
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198817966.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SaveZamer.sikuli/1580198835113.png")
    
    
           
    pass       

def ScenarioLine17():
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/ScenarioLine17.sikuli/1595108969152.png").targetOffset(-24,22))

def SelectStringsInText():
    type(Key.HOME)
    sleep(1)
    
    if len(sys.argv) == 2:
        KolStrok = int(sys_argv_1)
        Napravlenye = 'down'
    
    
    if len(sys.argv) == 3:
        KolStrok = -int(sys_argv_1)
        Napravlenye = 'up' 
    
    if KolStrok < 0:
       KolStrok = -KolStrok
    
    
    if Env.isLockOn(Key.NUM_LOCK):
        nlZap=True
    else:
        nlZap=False
    if nlZap: type(Key.NUM_LOCK)
    
    keyDown(Key.SHIFT)
    sleep(0.5)
    for n in range(0, KolStrok):
        if Napravlenye == 'up':
            type(Key.UP)
        else:
            type(Key.DOWN)
        sleep(0.1)
    
    keyUp()
    
    if nlZap: type(Key.NUM_LOCK)
    
    pass

def SetFlagStopOnFirstError():
    sleep(1)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/SetFlagStopOnFirstError.sikuli/OCTBHOBK3FID.png").targetOffset(-137,1))
    pass

def SourceTree():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/SourceTree.sikuli/DownloadSour.png",15):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/SourceTree.sikuli/DownloadSour.png")
        pass
    exit(1)

def StartRecBehavior():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartRecBehavior.sikuli/HSNSTI3SIHCb.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartRecBehavior.sikuli/HSNSTI3SIHCb.png")
    sleep(1)
    pass

def StartZamer():
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580195068422.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580195068422.png")
    
    
    if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580196282023.png"):
        click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580196282023.png")
        
        
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193456450.png")
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193473300.png")
    sleep(1)
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193506111.png")
    
    sleep(1)
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193456450.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193641655.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193668585.png")
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193691183.png").similar(0.60).targetOffset(-125,1))
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193722709.png").similar(0.77).targetOffset(-35,0)):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193722709.png").similar(0.77).targetOffset(-35,0))
    
    if exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580801201748.png").similar(0.80)):
        click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580801201748.png").similar(0.80).targetOffset(-40,0))
    
    
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193738511.png").similar(0.80).targetOffset(-41,0))
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193761791.png").similar(0.75).targetOffset(-40,-1))
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193778893.png").similar(0.75).targetOffset(-49,1))
    
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193795299.png")
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StartZamer.sikuli/1580193805208.png")
    
    
    
    
    pass

def StopRecBehavior():
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/StopRecBehavior.sikuli/33KOHlITb38F.png"):
        exit(1)
        
    click("C:/Commons/rep/vanessa-automation/tools/Sikuli/StopRecBehavior.sikuli/33KOHlITb38F.png")
    sleep(1)
    pass

def SvernutDerevoDoFich():
    rightClick(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/SvernutDerevoDoFich.sikuli/1463774011187.png").similar(0.60))
    sleep(1)
    hover(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/SvernutDerevoDoFich.sikuli/BBpHfTbADQJH.png").similar(0.50))
    sleep(0.5)
    pass

def SwitchToConf():
    kol = 0
    while True:
        FindIm = findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/SwitchToConf.sikuli/1465210805287.png") 
        ArrOfImage = list(FindIm)
        KolImages  = len(ArrOfImage)
        id = -1
        maxX = -1
        print 'KolImages='+ str(KolImages)
        for n in range(0, KolImages):
            t = ArrOfImage[n]
            print 't.x='+ str(t.x)
            if t.x > maxX:
                maxX = t.x
                id = n
        if KolImages > 0:
            t = ArrOfImage[id]
            print 'click t.x='+ str(t.x)
            click(Location(t.x+5,t.y+5))
            break
        sleep(1)
        kol = kol+1
        if kol > 5:
            exit(1)
    
    pass

def SwitchToTestClient():
    kol = 0
    while True:
        FindIm = findAll("C:/Commons/rep/vanessa-automation/tools/Sikuli/SwitchToTestClient.sikuli/HF.png") 
        ArrOfImage = list(FindIm)
        KolImages  = len(ArrOfImage)
        id = -1
        maxX = -1
        print 'KolImages='+ str(KolImages)
        for n in range(0, KolImages):
            t = ArrOfImage[n]
            print 't.x='+ str(t.x)
            if t.x > maxX:
                maxX = t.x
                id = n
        if KolImages > 0:
            t = ArrOfImage[id]
            print 'click t.x='+ str(t.x)
            click(Location(t.x+5,t.y+5))
            break
        sleep(1)
        kol = kol+1
        if kol > 5:
            exit(1)
    
    pass

def TypeEND():
    type(Key.END)
    pass

def TypeENTER():
    type(Key.ENTER)
    pass

def TypeESC():
    type(Key.ESC)
    pass

def TypeESC_END_ENTER_HOME():
    type(Key.ESC)
    type(Key.END)
    type(Key.ENTER)
    type(Key.HOME)
    
    pass

def TypeHome():
    type(Key.HOME)
    pass

def TypeTAB():
    type(Key.TAB)
    pass

def TypeTABTAB():
    type(Key.TAB)
    type(Key.TAB)
    pass

def TypeText():
    
    #paste(unicode(sys_argv_1,'utf-8'))
    #sleep(1)
    
    #print sys.argv[0]
    file = open(sys_argv_1, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        stroka = unicode(line, 'utf-8')
        if stroka == '#enter':
            type(Key.ENTER)
        else:
            paste(stroka)
            #App.setClipboard(stroka)
            #rightClick(Env.getMouseLocation())
            #sleep(0.5)
            #click("C:/Commons/rep/vanessa-automation/tools/Sikuli/TypeText.sikuli/Bcrasmu.png")
        sleep(0.5)
    sleep(1)    
    pass

def VscIsOpen():
    wait(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/1464017836667.png").similar(0.60),60)
    if not exists(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/1464017836667.png").similar(0.60)):
        exit(1)    
    
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/1464017836667.png").similar(0.60).targetOffset(18,2))
    
    #type("n",KeyModifier.CTRL)
    
    wait(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/115LIl1lliZn.png").similar(0.60),60)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/115LIl1lliZn.png").similar(0.60))
    wait(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/Zufspnmpn2mx.png").similar(0.60),30)
    click(Pattern("C:/Commons/rep/vanessa-automation/tools/Sikuli/VscIsOpen.sikuli/Zufspnmpn2mx.png").similar(0.60))
    
    
    sleep(1)
    paste("Gherkin")
    sleep(1)
    type(Key.ENTER)
    pass

def WaitForFeatureLoadInEditor():
    n = 6
    for x in range(n):
        if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/WaitForFeatureLoadInEditor.sikuli/1533560273739.png",1):
            pass
        if exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/WaitForFeatureLoadInEditor.sikuli/1532881364738.png",1):
            pass
    
    exit(1)

def WaitForStringAllScenariosOK():
    wait("C:/Commons/rep/vanessa-automation/tools/Sikuli/WaitForStringAllScenariosOK.sikuli/Bcecqevaapvw.png",120)
    if not exists("C:/Commons/rep/vanessa-automation/tools/Sikuli/WaitForStringAllScenariosOK.sikuli/Bcecqevaapvw.png"):
        exit(1)
        
    pass

def WaitPict():
    PictureToClick = sys_argv_1
    KolSec = int(sys_argv_2)
    wait(PictureToClick,KolSec)
    pass

def WheelCtrl():
    from java.awt import Robot
    robot = Robot()
    
    DirectionStr = sys_argv_1
    # up=1 or down=-1
    direction = -1
    if DirectionStr == 'up':
        direction = 1
        
    Kol = int(sys_argv_2)
    
    keyDown(Key.CTRL)
    sleep(0.1)
    for x in range(0, Kol):
      robot.mouseWheel(direction)
      sleep(0.1)
    
    keyUp()
      

def WriteText():
    # Посимвольный вывод символов
    def VyvestiStrokuPosimvolno(stroka):
        dlina = len(stroka)
        i = 0
        while i < dlina:
            tekSimvol = stroka[i]
            paste(tekSimvol)
            sleep(0.05)
            type('c', KeyModifier.CTRL)
            i = i + 1
            buf = Env.getClipboard()
            if i == dlina:
                sleep(1)
                continue
            if buf == tekSimvol:
                kkk = 0
                while kkk < 5:
                    type('c', KeyModifier.CTRL)
                    buf = Env.getClipboard()
                    kkk = kkk + 1
                    sleep(0.7)
                    if buf == '':
                        break
                
    
    # Паузы
    ShortBreak = 1
    MiddleBreak = 3
    BigBreak = 5
    
    step = sys_argv_1
    
    # Открытие текстового редактора
    if step == "1":
        type('r', KeyModifier.WIN)
        type(Key.DELETE)
        sleep(ShortBreak)
    #    paste(u"notepad++ -nosession")
        paste(u"code")
        sleep(MiddleBreak)
        type(Key.ENTER)
        sleep(MiddleBreak)
        pass
    # Ввод текста
    elif step == "2":
        #type('n', KeyModifier.CTRL)
        path2file = sys_argv_2
        file = open(path2file, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            stroka = unicode(line, 'utf-8')
            VyvestiStrokuPosimvolno(stroka)
        sleep(BigBreak)
        pass
    # Сохранение текста
    elif step == "3":
        path2VanessaBehavoirFeature = sys_argv_2
        type('s', KeyModifier.CTRL)
        sleep(2)
        type(Key.DELETE)
        sleep(1)
        paste(path2VanessaBehavoirFeature)
        sleep(1)
        pass
    elif step == "4":
        type(Key.ENTER)
        sleep(1)
        type(Key.F4, KeyModifier.CTRL)
        sleep(1)
        type(Key.F4, KeyModifier.ALT)
        sleep(BigBreak)
        pass
        


comand_filename   = sys.argv[1]
response_filename = sys.argv[2]
DoResponse(response_filename,"sikulix server started")
NeetToExit = False

while True:
    try:
        if not os.path.exists(comand_filename):
            sleep(0.3)
            continue
    except:
            continue
    
    
    with open(comand_filename) as data_file_comand:    
            dataofcomand = json.load(data_file_comand)
            comand = dataofcomand['comand']
            if comand == "exit0":
                NeetToExit = True
                break



            elif comand == "AtomIsOpen":
                read_comand(dataofcomand)
                AtomIsOpen()
                DoResponse(response_filename,'success')


            elif comand == "CallQueryConstructWithResult":
                read_comand(dataofcomand)
                CallQueryConstructWithResult()
                DoResponse(response_filename,'success')


            elif comand == "ChooseGherkin":
                read_comand(dataofcomand)
                ChooseGherkin()
                DoResponse(response_filename,'success')


            elif comand == "ClickButtonDobavit":
                read_comand(dataofcomand)
                ClickButtonDobavit()
                DoResponse(response_filename,'success')


            elif comand == "ClickButtonLoadFeatures":
                read_comand(dataofcomand)
                ClickButtonLoadFeatures()
                DoResponse(response_filename,'success')


            elif comand == "ClickButtonProvestiIZakrit":
                read_comand(dataofcomand)
                ClickButtonProvestiIZakrit()
                DoResponse(response_filename,'success')


            elif comand == "ClickButtonSozdat":
                read_comand(dataofcomand)
                ClickButtonSozdat()
                DoResponse(response_filename,'success')


            elif comand == "ClickContextMenuOpenFeatureInTextEditor":
                read_comand(dataofcomand)
                ClickContextMenuOpenFeatureInTextEditor()
                DoResponse(response_filename,'success')


            elif comand == "ClickContextMenuVisualStudioCode":
                read_comand(dataofcomand)
                ClickContextMenuVisualStudioCode()
                DoResponse(response_filename,'success')


            elif comand == "ClickCoordinates":
                read_comand(dataofcomand)
                ClickCoordinates()
                DoResponse(response_filename,'success')


            elif comand == "ClickFieldSkladPrihNakl":
                read_comand(dataofcomand)
                ClickFieldSkladPrihNakl()
                DoResponse(response_filename,'success')


            elif comand == "ClickFlagGenUF":
                read_comand(dataofcomand)
                ClickFlagGenUF()
                DoResponse(response_filename,'success')


            elif comand == "ClickFlagMakeOblast":
                read_comand(dataofcomand)
                ClickFlagMakeOblast()
                DoResponse(response_filename,'success')


            elif comand == "ClickGeneratorEPF":
                read_comand(dataofcomand)
                ClickGeneratorEPF()
                DoResponse(response_filename,'success')


            elif comand == "ClickMenuPrihNakl":
                read_comand(dataofcomand)
                ClickMenuPrihNakl()
                DoResponse(response_filename,'success')


            elif comand == "ClickOnPicture":
                read_comand(dataofcomand)
                ClickOnPicture()
                DoResponse(response_filename,'success')


            elif comand == "ClickRazdelOsnovnaya":
                read_comand(dataofcomand)
                ClickRazdelOsnovnaya()
                DoResponse(response_filename,'success')


            elif comand == "ClickRightOnPicture":
                read_comand(dataofcomand)
                ClickRightOnPicture()
                DoResponse(response_filename,'success')


            elif comand == "ClickSaveFF":
                read_comand(dataofcomand)
                ClickSaveFF()
                DoResponse(response_filename,'success')


            elif comand == "ClickServiceTab":
                read_comand(dataofcomand)
                ClickServiceTab()
                DoResponse(response_filename,'success')


            elif comand == "ClickTabScenariyPovedeniya":
                read_comand(dataofcomand)
                ClickTabScenariyPovedeniya()
                DoResponse(response_filename,'success')


            elif comand == "ClickToVspomogatelnayaTab":
                read_comand(dataofcomand)
                ClickToVspomogatelnayaTab()
                DoResponse(response_filename,'success')


            elif comand == "ClickUITab":
                read_comand(dataofcomand)
                ClickUITab()
                DoResponse(response_filename,'success')


            elif comand == "ClickWordScenario":
                read_comand(dataofcomand)
                ClickWordScenario()
                DoResponse(response_filename,'success')


            elif comand == "CloseConfigurator":
                read_comand(dataofcomand)
                CloseConfigurator()
                DoResponse(response_filename,'success')


            elif comand == "CloseMPC":
                read_comand(dataofcomand)
                CloseMPC()
                DoResponse(response_filename,'success')


            elif comand == "CloseNotePadPlusPlus":
                read_comand(dataofcomand)
                CloseNotePadPlusPlus()
                DoResponse(response_filename,'success')


            elif comand == "CloseProgrammsAfterTests":
                read_comand(dataofcomand)
                CloseProgrammsAfterTests()
                DoResponse(response_filename,'success')


            elif comand == "CloseWinExplorer":
                read_comand(dataofcomand)
                CloseWinExplorer()
                DoResponse(response_filename,'success')


            elif comand == "CollapseServiceArea":
                read_comand(dataofcomand)
                CollapseServiceArea()
                DoResponse(response_filename,'success')


            elif comand == "ConfiguratorIsOpen":
                read_comand(dataofcomand)
                ConfiguratorIsOpen()
                DoResponse(response_filename,'success')


            elif comand == "ContextMenu":
                read_comand(dataofcomand)
                ContextMenu()
                DoResponse(response_filename,'success')


            elif comand == "CtrlC":
                read_comand(dataofcomand)
                CtrlC()
                DoResponse(response_filename,'success')


            elif comand == "CtrlF":
                read_comand(dataofcomand)
                CtrlF()
                DoResponse(response_filename,'success')


            elif comand == "CtrlH":
                read_comand(dataofcomand)
                CtrlH()
                DoResponse(response_filename,'success')


            elif comand == "CtrlN":
                read_comand(dataofcomand)
                CtrlN()
                DoResponse(response_filename,'success')


            elif comand == "CtrlO":
                read_comand(dataofcomand)
                CtrlO()
                DoResponse(response_filename,'success')


            elif comand == "CtrlPlus":
                read_comand(dataofcomand)
                CtrlPlus()
                DoResponse(response_filename,'success')


            elif comand == "CtrlS":
                read_comand(dataofcomand)
                CtrlS()
                DoResponse(response_filename,'success')


            elif comand == "CtrlV":
                read_comand(dataofcomand)
                CtrlV()
                DoResponse(response_filename,'success')


            elif comand == "DeleteLineWithText":
                read_comand(dataofcomand)
                DeleteLineWithText()
                DoResponse(response_filename,'success')


            elif comand == "DoAltF4":
                read_comand(dataofcomand)
                DoAltF4()
                DoResponse(response_filename,'success')


            elif comand == "DoCtrlF4":
                read_comand(dataofcomand)
                DoCtrlF4()
                DoResponse(response_filename,'success')


            elif comand == "DoReplace":
                read_comand(dataofcomand)
                DoReplace()
                DoResponse(response_filename,'success')


            elif comand == "DoubleClickOnPicture":
                read_comand(dataofcomand)
                DoubleClickOnPicture()
                DoResponse(response_filename,'success')


            elif comand == "DragAndDrop":
                read_comand(dataofcomand)
                DragAndDrop()
                DoResponse(response_filename,'success')


            elif comand == "Exit1C":
                read_comand(dataofcomand)
                Exit1C()
                DoResponse(response_filename,'success')


            elif comand == "FeatureLoadMany":
                read_comand(dataofcomand)
                FeatureLoadMany()
                DoResponse(response_filename,'success')


            elif comand == "FeatureLoadOne":
                read_comand(dataofcomand)
                FeatureLoadOne()
                DoResponse(response_filename,'success')


            elif comand == "FirstFeature":
                read_comand(dataofcomand)
                FirstFeature()
                DoResponse(response_filename,'success')


            elif comand == "GenerateEPF":
                read_comand(dataofcomand)
                GenerateEPF()
                DoResponse(response_filename,'success')


            elif comand == "GetAll1CWindowsCoordinates":
                read_comand(dataofcomand)
                GetAll1CWindowsCoordinates()
                DoResponse(response_filename,'success')


            elif comand == "GetDebuggerUrl":
                read_comand(dataofcomand)
                GetDebuggerUrl()
                DoResponse(response_filename,'success')


            elif comand == "GetPictureCoordinats":
                read_comand(dataofcomand)
                GetPictureCoordinats()
                DoResponse(response_filename,'success')


            elif comand == "GetVideoClickDownload":
                read_comand(dataofcomand)
                GetVideoClickDownload()
                DoResponse(response_filename,'success')


            elif comand == "Git":
                read_comand(dataofcomand)
                Git()
                DoResponse(response_filename,'success')


            elif comand == "GoToEndOfLineWithShift":
                read_comand(dataofcomand)
                GoToEndOfLineWithShift()
                DoResponse(response_filename,'success')


            elif comand == "GoToEndOfModule":
                read_comand(dataofcomand)
                GoToEndOfModule()
                DoResponse(response_filename,'success')


            elif comand == "GoToFormModule":
                read_comand(dataofcomand)
                GoToFormModule()
                DoResponse(response_filename,'success')


            elif comand == "GoToProcedure":
                read_comand(dataofcomand)
                GoToProcedure()
                DoResponse(response_filename,'success')


            elif comand == "GoToTabScenarioRun":
                read_comand(dataofcomand)
                GoToTabScenarioRun()
                DoResponse(response_filename,'success')


            elif comand == "GoToTabService":
                read_comand(dataofcomand)
                GoToTabService()
                DoResponse(response_filename,'success')


            elif comand == "HotKey":
                read_comand(dataofcomand)
                HotKey()
                DoResponse(response_filename,'success')


            elif comand == "IGoToConditions":
                read_comand(dataofcomand)
                IGoToConditions()
                DoResponse(response_filename,'success')


            elif comand == "IGoToLeftSideOfConditions":
                read_comand(dataofcomand)
                IGoToLeftSideOfConditions()
                DoResponse(response_filename,'success')


            elif comand == "IGoToTablesAndFields":
                read_comand(dataofcomand)
                IGoToTablesAndFields()
                DoResponse(response_filename,'success')


            elif comand == "IPressOkInQueryConstruct":
                read_comand(dataofcomand)
                IPressOkInQueryConstruct()
                DoResponse(response_filename,'success')


            elif comand == "LoadingFeatureFileInBehavior":
                read_comand(dataofcomand)
                LoadingFeatureFileInBehavior()
                DoResponse(response_filename,'success')


            elif comand == "MoveActiveWindowFullScreen":
                read_comand(dataofcomand)
                MoveActiveWindowFullScreen()
                DoResponse(response_filename,'success')


            elif comand == "MoveActiveWindowLeft":
                read_comand(dataofcomand)
                MoveActiveWindowLeft()
                DoResponse(response_filename,'success')


            elif comand == "MoveActiveWindowRight":
                read_comand(dataofcomand)
                MoveActiveWindowRight()
                DoResponse(response_filename,'success')


            elif comand == "MoveMouseToPicture":
                read_comand(dataofcomand)
                MoveMouseToPicture()
                DoResponse(response_filename,'success')


            elif comand == "NotePadIsOpen":
                read_comand(dataofcomand)
                NotePadIsOpen()
                DoResponse(response_filename,'success')


            elif comand == "OpenBehavior":
                read_comand(dataofcomand)
                OpenBehavior()
                DoResponse(response_filename,'success')


            elif comand == "OpenDialog":
                read_comand(dataofcomand)
                OpenDialog()
                DoResponse(response_filename,'success')


            elif comand == "OpenDialogClick":
                read_comand(dataofcomand)
                OpenDialogClick()
                DoResponse(response_filename,'success')


            elif comand == "OpenDialogClickFolder":
                read_comand(dataofcomand)
                OpenDialogClickFolder()
                DoResponse(response_filename,'success')


            elif comand == "OpenDialogClickFolderSelect":
                read_comand(dataofcomand)
                OpenDialogClickFolderSelect()
                DoResponse(response_filename,'success')


            elif comand == "OpenDialogConf":
                read_comand(dataofcomand)
                OpenDialogConf()
                DoResponse(response_filename,'success')


            elif comand == "OpenFeatureFileInRedactor":
                read_comand(dataofcomand)
                OpenFeatureFileInRedactor()
                DoResponse(response_filename,'success')


            elif comand == "OpenFile":
                read_comand(dataofcomand)
                OpenFile()
                DoResponse(response_filename,'success')


            elif comand == "OpenMainFormOfEPF":
                read_comand(dataofcomand)
                OpenMainFormOfEPF()
                DoResponse(response_filename,'success')


            elif comand == "PictExists":
                read_comand(dataofcomand)
                PictExists()
                DoResponse(response_filename,'success')


            elif comand == "PressEnd":
                read_comand(dataofcomand)
                PressEnd()
                DoResponse(response_filename,'success')


            elif comand == "PressEndEnter":
                read_comand(dataofcomand)
                PressEndEnter()
                DoResponse(response_filename,'success')


            elif comand == "PressTab":
                read_comand(dataofcomand)
                PressTab()
                DoResponse(response_filename,'success')


            elif comand == "Python":
                read_comand(dataofcomand)
                Python()
                DoResponse(response_filename,'success')


            elif comand == "ReloadScenarios":
                read_comand(dataofcomand)
                ReloadScenarios()
                DoResponse(response_filename,'success')


            elif comand == "RunScenarios":
                read_comand(dataofcomand)
                RunScenarios()
                DoResponse(response_filename,'success')


            elif comand == "SaveChangesCtrls":
                read_comand(dataofcomand)
                SaveChangesCtrls()
                DoResponse(response_filename,'success')


            elif comand == "SaveZamer":
                read_comand(dataofcomand)
                SaveZamer()
                DoResponse(response_filename,'success')


            elif comand == "ScenarioLine17":
                read_comand(dataofcomand)
                ScenarioLine17()
                DoResponse(response_filename,'success')


            elif comand == "SelectStringsInText":
                read_comand(dataofcomand)
                SelectStringsInText()
                DoResponse(response_filename,'success')


            elif comand == "SetFlagStopOnFirstError":
                read_comand(dataofcomand)
                SetFlagStopOnFirstError()
                DoResponse(response_filename,'success')


            elif comand == "SourceTree":
                read_comand(dataofcomand)
                SourceTree()
                DoResponse(response_filename,'success')


            elif comand == "StartRecBehavior":
                read_comand(dataofcomand)
                StartRecBehavior()
                DoResponse(response_filename,'success')


            elif comand == "StartZamer":
                read_comand(dataofcomand)
                StartZamer()
                DoResponse(response_filename,'success')


            elif comand == "StopRecBehavior":
                read_comand(dataofcomand)
                StopRecBehavior()
                DoResponse(response_filename,'success')


            elif comand == "SvernutDerevoDoFich":
                read_comand(dataofcomand)
                SvernutDerevoDoFich()
                DoResponse(response_filename,'success')


            elif comand == "SwitchToConf":
                read_comand(dataofcomand)
                SwitchToConf()
                DoResponse(response_filename,'success')


            elif comand == "SwitchToTestClient":
                read_comand(dataofcomand)
                SwitchToTestClient()
                DoResponse(response_filename,'success')


            elif comand == "TypeEND":
                read_comand(dataofcomand)
                TypeEND()
                DoResponse(response_filename,'success')


            elif comand == "TypeENTER":
                read_comand(dataofcomand)
                TypeENTER()
                DoResponse(response_filename,'success')


            elif comand == "TypeESC":
                read_comand(dataofcomand)
                TypeESC()
                DoResponse(response_filename,'success')


            elif comand == "TypeESC_END_ENTER_HOME":
                read_comand(dataofcomand)
                TypeESC_END_ENTER_HOME()
                DoResponse(response_filename,'success')


            elif comand == "TypeHome":
                read_comand(dataofcomand)
                TypeHome()
                DoResponse(response_filename,'success')


            elif comand == "TypeTAB":
                read_comand(dataofcomand)
                TypeTAB()
                DoResponse(response_filename,'success')


            elif comand == "TypeTABTAB":
                read_comand(dataofcomand)
                TypeTABTAB()
                DoResponse(response_filename,'success')


            elif comand == "TypeText":
                read_comand(dataofcomand)
                TypeText()
                DoResponse(response_filename,'success')


            elif comand == "VscIsOpen":
                read_comand(dataofcomand)
                VscIsOpen()
                DoResponse(response_filename,'success')


            elif comand == "WaitForFeatureLoadInEditor":
                read_comand(dataofcomand)
                WaitForFeatureLoadInEditor()
                DoResponse(response_filename,'success')


            elif comand == "WaitForStringAllScenariosOK":
                read_comand(dataofcomand)
                WaitForStringAllScenariosOK()
                DoResponse(response_filename,'success')


            elif comand == "WaitPict":
                read_comand(dataofcomand)
                WaitPict()
                DoResponse(response_filename,'success')


            elif comand == "WheelCtrl":
                read_comand(dataofcomand)
                WheelCtrl()
                DoResponse(response_filename,'success')


            elif comand == "WriteText":
                read_comand(dataofcomand)
                WriteText()
                DoResponse(response_filename,'success')



    #f.close()
    os.remove(comand_filename)
        
    if NeetToExit:
        break
            
    sleep(0.3)        


exit(0)

