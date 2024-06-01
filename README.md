# Aron4

Welcome To **Aron4** A python 4 bit computer emulator Currently serving as a project to get me started on this topic once this project is done i will more than likely move on with the **Aron8** A 8 bit computer emulator!

# Limitations
- 8 bit address bus (Max of 255 Memory Locations)
- Maximum of 15 commands
- 300 **Hz**

# Commands
- sb - subtracts **Reg a** From **Reg c** and stores it in **Reg c**
- ad - adds **Reg a** to **Reg c** and stores it in **Reg c**
- ld - Loads **Address** from memory and into **Reg a**
> This is done by Using reg a and reg b together eg:
> Reg a: 0101
> Reg b: 0010
> This loads value 01010010 into reg a
- st - Stores **Reg c** into memory and into **Address (Reg a + reg b)**
- mv --- moves a item from **Target reg 1** into **Target reg 2**
> This is done by reading of the stack and using the vaue as the 2 arguments eg:
> 1001 Will move **Register c** to **Register a**


# Errors
- 0000 --- File is too big
- 0001 --- File Execution error
- 0010 ---
- 0011 ---
- 0100 --- File Loading error
