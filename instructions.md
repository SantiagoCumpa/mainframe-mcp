# Instructions
This is the guide to understand the mainframe structure used in this project.

## Mainframe Structure
A library from host is componed of:
```
<AMB>.LIB.<LIBR>(<MEMBER>)

Where:
<AMB> -> Environment
<LIBR> -> Library
<MEMBER> -> Component
```

### Environment:
- E: Production
- A: UAT (Testing)
- I: Integration
- D: Development

### Library:
- PROGRAM: Programs
- COPY.COB: Copybooks
- PARM: Parameters
- PROC: Procedures
- JCL/JOB: Jobs
- JOB.ALT: Job Alternatives
- DCL.DB2: DCL for DB2 Tables
- PLAN.DB2: Plan for DB2 Programs and Transactions

### Member:
- Actual name of the member/component

### Examples of mainframe structure:
Example:

| Mainframe Structure          | Description                                 |
|------------------------------|---------------------------------------------|
| `E.LIB.PROGRAM(CDIOI24)`     | Production environment, Program CDIOI24     |
| `A.LIB.COPY.COB(CDICI024)`   | UAT environment, Copybook CDICI024          |
| `I.LIB.JCL(JCLCDI24)`        | Integration environment, Job JCLCDI24       |
| `D.LIB.PARM(PARM123)`        | Development environment, Parameter PARM123  |
| `A.LIB.DCL.DB2(CDTT123)`     | UAT environment, DCL for table CDDT123      |