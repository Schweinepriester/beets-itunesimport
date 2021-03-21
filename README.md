# beets-itunesimport

Plugin for beets to automatically add imported albums to iTunes, using the iTunes COM Interface on Windows.

Only tested on Win10 with iTunes 10.7 for now.

## Troubleshooting

### AttributeError: `… no attribute 'CLSIDToClassMap'`

E.g.

```powershell
AttributeError: module 'win32com.gen_py.9E93C96F-CF0D-43F6-8BA8-B807A3370712x0x1x13' has no attribute 'CLSIDToClassMap'
```

Answers ([1](https://stackoverflow.com/questions/59276808/win32com-module-problems), [2](https://stackoverflow.com/questions/52889704/python-win32com-excel-com-model-started-generating-errors)) on Stack Overflow
 suggested deleting folders in

```
%USERPROFILE%\AppData\Local\Temp\gen_py
```

which worked for me.
