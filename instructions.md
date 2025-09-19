A library from host is componed of:

<AMB> -> Environment
<LIBRARY> -> Component Library
<MEMBER> -> Component

Environment:
- E: Production
- A: UAT (Testing)
- I: Integration
- D: Development

Library:
- PROGRAM: Programs
- COPY.COB: Copybooks
- PARM: Parameters
- PROC: Procedures
- JCL/JOB: Jobs
- JOB.ALT: Job Alternatives
- DCL.DB2: DCL for DB2 Tables
- PLAN.DB2: Plan for DB2 Programs and Transactions

Member:
- Actual name of the member/component

Structure:
<AMB>.LIB.<LIBRARY>(<MEMBER>)

Example:
E.LIB.PROGRAM(CDIOI24) -> On Production environment, Program CDIOI24
A.LIB.COPY.COB(CDICI024) -> On UAT environment, Copybook CDICI024
I.LIB.JCL(JCLCDI24) -> On Integration, Job JCLCDI24
D.LIB.PARM(PARCDI24) -> On Development, Parameter PARCDI24