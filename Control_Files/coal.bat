for %%a in (10,11,20,21,30,31,40,41,50,51) do (
	gemsim -cmf Control_Files\coal.cmf -p1=%%a
	sltoht -sti Control_Files\coal%%a.sti
)