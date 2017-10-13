for %%a in (01,01) do (
	gemsim -cmf Control_Files\coal.cmf -p1=%%a
	sltoht -sti Control_Files\coal%%a.sti
)