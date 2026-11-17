import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leggi il dataset
    df = pd.read_csv('adult.data.csv')

    # 1. Quante persone di ogni razza sono rappresentate in questo dataset? (Serie Pandas con i nomi delle razze come indice)
    race_count = df['race'].value_counts()

    # 2. Qual è l'età media degli uomini?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Qual è la percentuale di persone che hanno una laurea triennale (Bachelors)?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Qual percentuale di persone con un'educazione avanzata (Bachelors, Masters, Doctorate) guadagna più di 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentuale con educazione avanzata che guadagna >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Qual percentuale di persone senza un'educazione avanzata guadagna più di 50K?
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Qual è il numero minimo di ore lavorate a settimana?
    min_work_hours = df['hours-per-week'].min()

    # 7. Qual percentuale delle persone che lavorano il minor numero di ore a settimana guadagna più di 50K?
    num_min_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round((df[num_min_workers]['salary'] == '>50K').mean() * 100, 1)

    # 8. Quale paese ha la più alta percentuale di persone che guadagnano >50K e qual è questa percentuale?
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_totals = df['native-country'].value_counts()
    highest_earning_country_percentage = (country_earnings / country_totals * 100).dropna()
    
    highest_earning_country = highest_earning_country_percentage.idxmax()
    highest_earning_country_percentage = round(highest_earning_country_percentage.max(), 1)

    # 9. Identifica l'occupazione più popolare per chi guadagna >50K in India.
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
