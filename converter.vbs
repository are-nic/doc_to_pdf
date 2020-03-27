Const wdFormatText = 17                                                  'выбираем формат, в который будем конвертировать'                        
Set objWord = CreateObject("Word.Application")
objWord.Visible = TRUE                                                  'открывается word'
On Error Resume Next
Set objDoc = objWord.Documents.Open(Wscript.Arguments.Item(0), True)    'открываем два раза файл, который конвертируем...'
Set objDoc = objWord.Documents.Open(Wscript.Arguments.Item(0), True)    '...в случае, когда все ок, файл откроется 2 раза, а в случае ошибки просто продолжит открытие файла'
objDoc.SaveAs WScript.Arguments.Item(1), wdFormatText
objWord.Quit


'формат конвертации выбирается в соответствии с таблицей https://docs.microsoft.com/en-us/office/vba/api/word.wdsaveformat'