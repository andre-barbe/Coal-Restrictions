for %%a in (10,20) do (
	gemsim -cmf Control_Files\coal.cmf -p1=%%a
pause
	sltoht -sti Control_Files\coal%%a.sti
pause)