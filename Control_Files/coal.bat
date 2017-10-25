for %%a in (10,20,30,40,11,21,31,41,00) do (
	gemsim -cmf Control_Files\coal.cmf -p1=%%a
	sltoht -sti Control_Files\coal%%a.sti
)