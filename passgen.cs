using System;

class SimplePasswordGenerator
{
    static void Main()
    {
        Console.Write("Enter password length: ");
        int length = int.Parse(Console.ReadLine());

        string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
        Random rand = new Random();
        string password = "";

        for (int i = 0; i < length; i++)
        {
            int index = rand.Next(chars.Length);
            password += chars[index];
        }

        Console.WriteLine($"Generated password: {password}");
    }
}
