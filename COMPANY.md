# Sprout Labs and Leaf & Pot

**Sprout Labs** is a five-person startup in Bahrain. We build and run **Leaf & Pot**, an online
plant shop that delivers indoor plants, pots and care kits across the island.

## The team
| Name | Role | Ask them about |
|---|---|---|
| Lina Haddad | Engineering manager, co-founder | priorities, deadlines, being stuck |
| Omar Khalil | Senior engineer | the code, Flask, how to approach a task |
| Sara Nasser | QA engineer | how something should behave, failing checks |
| Yousef Amin | Product manager | what customers need and why |
| Rana Saleh | People and operations | how the internship works, your workload |

## The product: Plant Box
Customers keep asking for "a new plant every month" without having to choose. Plant Box is
our answer: pick a plan, and a plant with its pot and care card arrives each month.

### The founder's brief
1. A Plant Box page at `/box` that names the product and its three plans.
2. Three plans, Starter, Grower and Jungle, each with a monthly price, kept in one place in
   the code.
3. A plans page that lists every plan with its price.
4. A footer on every page that says who built the site.
5. A "How it works" page in three steps: Choose, Receive, Grow.
6. A signup form (name, email, plan) that rejects a bad email or a plan we don't sell.
7. Signups saved in the database, and a thank-you page that greets the customer by name.
8. Yearly billing at a discount, shown next to the monthly prices.
9. "Which plan fits me?": the customer describes their sunlight and space, and AI suggests a
   plan. If the AI is down, a fixed helpful answer instead.
10. An admin page for the founder, behind a password: all subscribers and how many chose
    each plan.

The exact paths, texts and numbers for each item are on your task page in Darbni.

## House rules
- Money is stored in **fils** as integers (1 BHD = 1000 fils) and shown as BHD with 3
  decimals: `7.500 BHD`.
- Times are Bahrain time (`Asia/Bahrain`). The weekend is Friday and Saturday.
- All code lives in the `plantbox` package. Keep functions small and names clear.
- AI only through `plantbox/ai.py` (see README), always with a fallback.
- Run `pytest` and click through the page in your browser before you submit.
