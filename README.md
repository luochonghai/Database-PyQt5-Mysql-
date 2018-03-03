PJ_Of_Accounting_Books
====
1.Description
----
      Based on mysql5.7 and PyQt5, it's developed for financial staff to process data in a more convenient way.
2.Improvement
----
      180302：to solve the problem of calculation in 成本明细, where negative numbers and decimals can't be ca-
      lculated correctly.
      Plan1:to use mysql's type--decimal(a,b) to solve the problem; to check whether decimals(without other ch-
      aracters) are input before data storing.
      Plan2:to write another routine to process negative or decimals calculation.<br>
      180303:choose Plan1 and finish it roughly.
