! closure for ALTERTAX simulation
Exogenous ! Part of closure for altertax runs
           pop
          psaveslack pfactwld
          profitslack incomeslack endwslack tradslack
          ams atm atf ats atd
          aosec aoreg avasec avareg
          afcom afsec afreg afecom afesec afereg
          aoall afall afeall
          au dppriv dpgov dpsave
          to tp tm tms tx txs
          qo(ENDW_COMM,REG) 
!    DTBAL exogenous for all regions except one,
!    and SAVESLACK exogenous for that one region (which can be any one).

dtbalr("USA")
dtbalr("EU27")
dtbalr("EEFSU")
dtbalr("JPN")
dtbalr("RoA1")
dtbalr("EEx")
dtbalr("CHN")
dtbalr("IND")
cgdslack("ROW");
Rest endogenous;
