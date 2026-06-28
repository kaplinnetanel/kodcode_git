using System;
using System.Security.Cryptography.X509Certificates;
namespace AccountManagement;

enum AccountTypes
{
    Savings, 
    Checking, 
    Business,

}

class BankAccount
{
    private int _accountNumber;
    private string _ownerName;
    private double _balance;
    private AccountTypes _accountType;
    private bool _isActive = true;
    private List<string> _transactionHistory;


    public int AccountNumber
    {
        get => _accountNumber;
    }

    public string OwnerName
    {
        get => _ownerName;

        set
        {
            if (string.IsNullOrWhiteSpace(value))
                {
                _ownerName = "Unknown";  
                }
            else
                {
                _ownerName = value;
                }

        }
    }
    public double Balance
    {
        get => _balance;

        set
        {
            if (value < 0)
            { _balance = 0; }
            else
            { _balance = value; }
        }
    }

    public string AccountType
    {
        get => _accountType.ToString();

        set 
        {
            if (Enum.TryParse<AccountTypes>(value, true,out AccountTypes result))
            {
                _accountType = result;
            }
            else
            {
                _accountType = AccountTypes.Checking;
            }
        }
  
    }
    public bool IsActive
    {
        get => _isActive;

        set
        {
            if (value)
            { _isActive = true; }
            else
            { _isActive = false; }
        }
    }

    public BankAccount(int accountNumber, string ownerName, double balance, string
accountType)
        {
         _accountNumber = accountNumber;
         OwnerName = ownerName;
         Balance = balance;
       
        _isActive = true;
        _transactionHistory = new List<string>();
    }
    public BankAccount(int accountNumber, string ownerName)
        : this(accountNumber, ownerName, 0.0, "Checking")
    {
        Console.WriteLine("Hello welcome");
    }
    

    public override string ToString()
    {
        return $"Account #{AccountNumber} | Owner: {OwnerName} | Balance: {Balance } F2 | Type: {AccountType}";
    }

    public void Deposit(double amount)
    {
        if (!_isActive)
        {
            Console.WriteLine("Error: Account is inactive."); 
            return; 
        }
         if (amount > 0)
        {
            Balance += amount;
            _transactionHistory.Add($"Deposited: ${amount:F2}");
        }
        else
        {
            Console.WriteLine("Error: Deposit amount must be positive.");
        }
    }

    public bool Withdraw(double amount)
    {
        if (!_isActive) 
        {
            Console.WriteLine("Error: Account is inactive.");
            return false; 
        }
        if (amount > 0 && Balance >= amount)
        {
            Balance -= amount;
            _transactionHistory.Add($"Withdrew: ${amount:F2}");
            return true;
        }
        Console.WriteLine("Error: Invalid amount or insufficient balance.");
        return false;
    }

    public void ApplyInterest()
    {
        if (_accountType == AccountTypes.Savings)
        {
            double interest = Balance * 0.02;
            Balance += interest;
            _transactionHistory.Add($"Interest applied: ${interest:F2}");
        }
    }


    public void PrintTransactionHistory()
    {
        Console.WriteLine($"Transaction History for {OwnerName}:");
        foreach (var transaction in _transactionHistory)
        {
            Console.WriteLine(transaction);
        }
    }
    public void Activate()
    { IsActive = true; }

    public void Deactivate()
    { IsActive = false; }

    public static bool Transfer(BankAccount from, BankAccount to, double amount)
    {
        if (from.IsActive && to.IsActive && amount > 0 && from.Balance >= amount)
        {
            from.Withdraw(amount);
            to.Deposit(amount);
            return true;
        }
        Console.WriteLine("Transfer failed: Invalid account status or insufficient funds.");
        return false;
    }
    

    static void Main()

    {
        List<BankAccount> accounts = new List<BankAccount>();

        accounts.Add(new BankAccount(1, "Netanel", 1000.0, "Savings"));
        accounts.Add(new BankAccount(2, "Dana", 500.0, "Checking"));
        accounts.Add(new BankAccount(3, "Moshe", 2000.0, "Business"));
        accounts.Add(new BankAccount(4, "Yossi"));
        accounts.Add(new BankAccount(5, "Tali", 100.0, "Savings"));

        BankAccount testAcc = new BankAccount(6, "", -50.0, "Crypto");
        Console.WriteLine(testAcc.ToString());

        foreach (BankAccount acc in accounts)
        {
            acc.ApplyInterest();
        }
        BankAccount.Transfer(accounts[0], accounts[1], 200);
        BankAccount b = new BankAccount(12345, "Netanel", 1000.5, "Savings");


        accounts[0].PrintTransactionHistory();
        accounts[1].PrintTransactionHistory();

        Console.WriteLine("\n--- Displaying All Accounts ---");
        foreach (BankAccount acc in accounts)
        {
            Console.WriteLine(acc.ToString());
        }

        Console.WriteLine(b.ToString());


    }

}
