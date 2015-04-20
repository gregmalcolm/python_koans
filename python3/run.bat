@echo off

REM This is how you run it from the command line.
REM You don't actually need this script!
SET RUN_KOANS=python.exe -B contemplate_koans.py

REM Set this to your python folder:
SET PYTHON_PATH=C:\Python34

set SCRIPT=

:loop

REM Hunt around for python
IF EXIST "python.exe" (
  SET SCRIPT=%RUN_KOANS%
) ELSE (
  IF EXIST "%PYTHON_PATH%" (
    SET SCRIPT=%PYTHON_PATH%\%RUN_KOANS%
  ) ELSE (
    IF EXIST %PYTHON% SET SCRIPT=%PYTHON%\%RUN_KOANS%
  )
)

IF NOT "" == "%SCRIPT%" (
  %SCRIPT%
  pause
) ELSE (
  echo.
  echo Python.exe is not in the path!
  echo.
  echo Fix the path and try again.
  echo Or better yet, run this with the correct python path:
  echo.
  echo   python.exe contemplate_koans.py
  pause
)

Set /p  keepgoing="Test again? y or n - "
if "%keepgoing%" == "y" (
	goto loop
	)

:end
