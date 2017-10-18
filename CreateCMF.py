__author__ = "Andre Barbe"
__project__ = "Coal Restrictions"
__created__ = "2017-10-6"
__altered__ = "2017-10-18"


class CreateCMF(object):
    """Creates the CMF File"""

    __slots__ = ["project", "solution_method"]

    def __init__(self, project: str, solution_method: str) -> None:
        self.project = project
        self.solution_method = solution_method

    def create(self) -> None:

        # Create important lines that you need to worry about
        if self.solution_method == "default_j":
            method_list = ["Method = Johansen;\n",
                           "Steps = 1;\n",
                           "automatic accuracy = no;\n",
                           "subintervals = 1;\n"]
        elif self.solution_method == "default_g":
            method_list = ["Method = Gragg;",
                           "Steps = 6 12 18;",
                           "automatic accuracy = yes;",
                           "accuracy figures = 4;",
                           "accuracy percent = 80;",
                           "minimum subinterval length =  1.0E-0003;",
                           "minimum subinterval fails = stop;",
                           "accuracy criterion = Data;",
                           "subintervals = 6;"]
        else:
            raise ValueError('Unknown solution method in CMF')

        # Create unimportant lines and combine them with important lines
        line_list = ["! This Command file\n",
                     "! c:\\rungtap5\\andreb\work\coaltest.cmf\n",
                     # Double \\ are required to escape the special character(s)
                     "! was written by RunGTAP (Version 3.61 built 19/Oct/2013)\n",
                     "! This is the default CMFSTART file which RunGTAP uses when\n",
                     "! a version has no CMFSTART file of its own\n",
                     "iz1 = no ;\n",
                     "NDS = yes; ! no displays\n",
                     "Extrapolation accuracy file = YES ;\n",
                     "CPU = yes;\n",
                     "!@ end of CMFSTART part\n",
                     "aux files = GTAP_Files\GTAP;\n",
                     "file gtapSETS = GTAP_Files\sets.har;\n",
                     "file gtapDATA = GTAP_Files\\basedata.har;\n",
                     # Double \\ are required to escape the special character
                     "Updated file gtapDATA = GTAP_Files\SaveSims\cresult<p1>.upd;\n",
                     "Solution file = GTAP_Files\SaveSims\coal<p1>;\n",
                     "file gtapPARM = GTAP_Files\default.prm;\n",
                     "Verbal Description =\n",
                     "<p1> pct reduction in coal intensity by electricity in US;\n"] + method_list + [
                        "! basic closure\n",
                        "exogenous\n",
                        "    afall\n",
                        "    afcom\n",
                        "    afreg\n",
                        "    afsec    \n",
                        "    ams\n",
                        "    aoall\n",
                        "    aoreg\n",
                        "    aosec\n",
                        "  ! atall               omitted\n",
                        "    atd\n",
                        "    atf\n",
                        "    atm\n",
                        "    ats\n",
                        "    au\n",
                        "    cgdslack\n",
                        "    del_ctgshr\n",
                        "    dpgov\n",
                        "    dppriv\n",
                        "    dpsave\n",
                        "    endwslack\n",
                        "    incomeslack\n",
                        "    pemp\n",
                        "    pfactwld\n",
                        "    pop\n",
                        "    profitslack\n",
                        "    psaveslack\n",
                        "    qo(ENDW_COMM,REG)\n",
                        "    RCTAXB\n",
                        "  ! tf                  omitted\n",
                        "    tfd\n",
                        "    tfm\n",
                        "    tgd\n",
                        "    tgm\n",
                        "    tm\n",
                        "    tms\n",
                        "    to\n",
                        "    tpd\n",
                        "    tpm\n",
                        "    tp\n",
                        "    tradslack\n",
                        "    tx\n",
                        "    txs\n",
                        "    pf_slack(FIRM_COMM,PROD_COMM,NUS_REG)\n",
                        "    pf_slack(NEF_COMM,NEP_COMM,US_REG)\n",
                        "    pf_slack(NEF_COMM,EGY_COMM,US_REG)\n",
                        "    pf_slack(EGY_COMM,NEP_COMM,US_REG)\n",
                        "pf_slack(\"Coal\",\"Coal\",US_REG)\n",  # \ is required to escape the quotes
                        "pf_slack(\"Coal\",\"Oil\",US_REG)\n",
                        "pf_slack(\"Coal\",\"Gas\",US_REG)\n",
                        "pf_slack(\"Coal\",\"Oil_pcts\",US_REG)\n",
                        "!pf_slack(\"Coal\",\"Electricity\",US_REG)\n",
                        "pf_slack(\"Oil\",\"Coal\",US_REG)\n",
                        "pf_slack(\"Oil\",\"Oil\",US_REG)\n",
                        "pf_slack(\"Oil\",\"Gas\",US_REG)\n",
                        "pf_slack(\"Oil\",\"Oil_pcts\",US_REG)\n",
                        "pf_slack(\"Oil\",\"Electricity\",US_REG)\n",
                        "pf_slack(\"Gas\",\"Coal\",US_REG)\n",
                        "pf_slack(\"Gas\",\"Oil\",US_REG)\n",
                        "pf_slack(\"Gas\",\"Gas\",US_REG)\n",
                        "pf_slack(\"Gas\",\"Oil_pcts\",US_REG)\n",
                        "pf_slack(\"Gas\",\"Electricity\",US_REG)\n",
                        "pf_slack(\"Oil_pcts\",\"Coal\",US_REG)\n",
                        "pf_slack(\"Oil_pcts\",\"Oil\",US_REG)\n",
                        "pf_slack(\"Oil_pcts\",\"Gas\",US_REG)\n",
                        "pf_slack(\"Oil_pcts\",\"Oil_pcts\",US_REG)\n",
                        "pf_slack(\"Oil_pcts\",\"Electricity\",US_REG)\n",
                        "pf_slack(\"Electricity\",\"Coal\",US_REG)\n",
                        "pf_slack(\"Electricity\",\"Oil\",US_REG)\n",
                        "pf_slack(\"Electricity\",\"Gas\",US_REG)\n",
                        "pf_slack(\"Electricity\",\"Oil_pcts\",US_REG)\n",
                        "pf_slack(\"Electricity\",\"Electricity\",US_REG)\n",
                        "intf(\"Coal\",\"Electricity\",US_REG)\n",
                        "\n",
                        "\n",
                        "\n",
                        "\n",
                        "    ;\n",
                        "Rest Endogenous ;\n",
                        "shock intf(\"Coal\",\"Electricity\",\"usa\") = -<p1>;\n"]

        # Create final file
        with open("Control_Files\{0}.cmf".format(self.project), "w+") as writer:  # Create the empty file
            writer.writelines(line_list)  # write the line list to the file
