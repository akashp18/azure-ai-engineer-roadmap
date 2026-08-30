# Azure Environment Setup Guide

Before you can build real AI applications and prepare for the AI-102 certification, you must configure your Microsoft Azure environment. This guide walks you through the 3 mandatory steps.

## Step 1: Create a Free Azure Account

You need an active Azure subscription to provision resources.
1. Go to [azure.microsoft.com/free](https://azure.microsoft.com/en-us/free/).
2. Click **Start free** and sign in with a Microsoft account.
3. Follow the identity verification steps (a credit card is required to verify identity, but you will not be charged unless you manually upgrade to a pay-as-you-go subscription).
4. You will receive $200 in free credits for your first 30 days!

## Step 2: Request Access to Azure OpenAI

Unlike most Azure services, Microsoft tightly controls access to Azure OpenAI to ensure responsible AI usage. **You must apply for access before you can use it.**

1. Log in to the [Azure Portal](https://portal.azure.com/).
2. Search for **Subscriptions** in the top search bar and copy your **Subscription ID**.
3. Go to the [Request Access to Azure OpenAI Service form](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUNTZBNzRKNlVQSFhZMU9aV09EVzlsT0xFViQlQCN0PWcu).
4. Fill out the form. You will need to provide your Subscription ID.
*(Note: Approval usually takes 24 to 48 hours. While you wait, you can still practice with other Cognitive Services like Vision and Speech).*

## Step 3: Install the Azure CLI

The Azure Command-Line Interface (CLI) is required to authenticate your local development environment so your Python code can securely talk to Azure without hardcoding passwords in your scripts.

### For Mac Users
Run Microsoft's direct installation script in your terminal:
```bash
curl -L https://aka.ms/InstallAzureCli | bash
```
*(If you have Homebrew installed, you can also use `brew update && brew install azure-cli`)*

### For Windows Users
Download and install the MSI installer from the [official documentation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows).

### Verify Installation
Once installed, open a new terminal window and verify the installation by typing:
```bash
az version
```

Finally, log in to connect your terminal to your Azure account:
```bash
az login
```
A browser window will open asking you to sign in. Once signed in, your environment is officially ready!
