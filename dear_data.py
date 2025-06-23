import numpy as np
import matplotlib.pyplot as plt

# Dear Data: Personal Observable Activity Tracking
# Inspiration: Track something you do daily that can be measured with numbers

def track_coffee_consumption():
    """
    Track coffee consumption throughout the day for a week
    🍵 Recording cups of coffee consumed each hour during waking hours
    """
    print("=== COFFEE CONSUMPTION TRACKING ===")
    
    # Simulated data: Cups of coffee per hour (7 AM to 11 PM) for 7 days
    # 1 = one cup, 0 = no coffee, 2 = two cups (rare!)
    coffee_data = np.array([
        # Mon  Tue  Wed  Thu  Fri  Sat  Sun
        [1,   1,   1,   1,   1,   0,   0],  # 7 AM
        [0,   0,   1,   0,   0,   1,   1],  # 8 AM
        [1,   1,   0,   1,   1,   1,   0],  # 9 AM
        [0,   1,   1,   0,   0,   0,   1],  # 10 AM
        [0,   0,   0,   1,   0,   0,   0],  # 11 AM
        [0,   0,   0,   0,   1,   0,   0],  # 12 PM
        [1,   1,   1,   1,   0,   0,   1],  # 1 PM
        [0,   0,   0,   0,   1,   1,   0],  # 2 PM
        [0,   1,   0,   0,   0,   0,   0],  # 3 PM
        [0,   0,   0,   1,   0,   0,   0],  # 4 PM
        [0,   0,   0,   0,   0,   0,   0],  # 5 PM
        [0,   0,   0,   0,   0,   0,   0],  # 6 PM
        [0,   0,   0,   0,   0,   0,   0],  # 7 PM
        [0,   0,   0,   0,   0,   0,   0],  # 8 PM
        [0,   0,   0,   0,   0,   0,   0],  # 9 PM
        [0,   0,   0,   0,   0,   0,   0],  # 10 PM
    ])
    
    print(f"Coffee data shape: {coffee_data.shape} (16 hours × 7 days)")
    print("Data structure: 2D array makes sense because we're tracking:")
    print("- Dimension 1: Time (hours of the day)")
    print("- Dimension 2: Days of the week")
    print()
    
    # Analysis using indexing and slicing
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Daily totals using slicing
    daily_totals = np.sum(coffee_data, axis=0)
    print("Daily coffee consumption:")
    for i, day in enumerate(days):
        print(f"  {day}: {daily_totals[i]} cups")
    
    # Average during waking hours
    avg_daily = np.mean(daily_totals)
    print(f"\nAverage cups per day: {avg_daily:.2f}")
    
    # Difference between beginning and end of week
    week_change = daily_totals[-1] - daily_totals[0]  # Sunday - Monday
    print(f"Change from Monday to Sunday: {week_change:+d} cups")
    
    # Peak coffee times
    hourly_totals = np.sum(coffee_data, axis=1)
    peak_hour = np.argmax(hourly_totals)
    print(f"Peak coffee hour: {peak_hour + 7}:00 ({7 + peak_hour}:00)")
    
    return coffee_data, daily_totals

def track_phone_pickups():
    """
    Track phone pickups per hour during waking hours
    📱 How many times you picked up your phone each hour
    """
    print("\n=== PHONE PICKUP TRACKING ===")
    
    # 1D array: Total phone pickups per day for a week
    # This could be 1D since we're just tracking daily totals
    daily_pickups = np.array([47, 52, 38, 61, 45, 73, 69])
    
    print(f"Phone pickup data shape: {daily_pickups.shape}")
    print("Data structure: 1D array makes sense because we're only tracking:")
    print("- One value per day (total pickups)")
    print()
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    print("Daily phone pickups:")
    for i, day in enumerate(days):
        print(f"  {day}: {daily_pickups[i]} pickups")
    
    # Analysis using indexing and slicing
    weekdays = daily_pickups[0:5]  # Monday to Friday
    weekend = daily_pickups[5:7]   # Saturday and Sunday
    
    print(f"\nWeekday average: {np.mean(weekdays):.1f} pickups")
    print(f"Weekend average: {np.mean(weekend):.1f} pickups")
    
    # Difference between beginning and end
    week_change = daily_pickups[-1] - daily_pickups[0]
    print(f"Change from Monday to Sunday: {week_change:+d} pickups")
    
    # Find patterns
    max_day_idx = np.argmax(daily_pickups)
    min_day_idx = np.argmin(daily_pickups)
    print(f"Highest usage: {days[max_day_idx]} ({daily_pickups[max_day_idx]} pickups)")
    print(f"Lowest usage: {days[min_day_idx]} ({daily_pickups[min_day_idx]} pickups)")
    
    return daily_pickups

def track_steps():
    """
    Track steps taken each hour during active hours
    👟 Recording steps per hour from 6 AM to 10 PM
    """
    print("\n=== STEP TRACKING ===")
    
    # 2D array: Steps per hour for a week (16 active hours × 7 days)
    np.random.seed(123)  # For consistent results
    
    # Simulate realistic step patterns
    base_steps = np.random.normal(200, 100, size=(16, 7))
    base_steps = np.clip(base_steps, 0, 2000)  # Keep realistic
    
    # Add morning and evening peaks
    base_steps[1:3, :] += np.random.normal(300, 50, size=(2, 7))  # Morning commute
    base_steps[9:11, :] += np.random.normal(400, 100, size=(2, 7))  # Lunch break
    base_steps[13:15, :] += np.random.normal(350, 75, size=(2, 7))  # Evening activities
    
    steps_data = np.round(base_steps).astype(int)
    
    print(f"Steps data shape: {steps_data.shape} (16 hours × 7 days)")
    print("Data structure: 2D array makes sense for detailed hour-by-hour tracking")
    print()
    
    # Daily totals
    daily_totals = np.sum(steps_data, axis=0)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    print("Daily step totals:")
    for i, day in enumerate(days):
        print(f"  {day}: {daily_totals[i]:,} steps")
    
    # Average during active hours
    avg_daily = np.mean(daily_totals)
    print(f"\nAverage steps per day: {avg_daily:,.0f}")
    
    # Time-based analysis
    morning_steps = np.sum(steps_data[0:4, :])  # 6-10 AM
    afternoon_steps = np.sum(steps_data[4:10, :])  # 10 AM-4 PM
    evening_steps = np.sum(steps_data[10:16, :])  # 4-10 PM
    
    total_steps = morning_steps + afternoon_steps + evening_steps
    print(f"Morning steps (6-10 AM): {morning_steps:,} ({morning_steps/total_steps*100:.1f}%)")
    print(f"Afternoon steps (10 AM-4 PM): {afternoon_steps:,} ({afternoon_steps/total_steps*100:.1f}%)")
    print(f"Evening steps (4-10 PM): {evening_steps:,} ({evening_steps/total_steps*100:.1f}%)")
    
    # Week progression
    week_change = daily_totals[-1] - daily_totals[0]
    print(f"\nChange from Monday to Sunday: {week_change:+,} steps")
    
    return steps_data, daily_totals

def visualize_all_data(coffee_data, coffee_daily, phone_pickups, steps_data, steps_daily):
    """Create visualizations for all tracked data"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Coffee consumption heatmap
    im1 = axes[0, 0].imshow(coffee_data, cmap='YlOrBr', aspect='auto')
    axes[0, 0].set_title('Coffee Consumption (Hourly)')
    axes[0, 0].set_xlabel('Day')
    axes[0, 0].set_ylabel('Hour (7 AM = 0)')
    axes[0, 0].set_xticks(range(7))
    axes[0, 0].set_xticklabels(days)
    plt.colorbar(im1, ax=axes[0, 0], label='Cups')
    
    # Daily coffee totals
    axes[0, 1].bar(range(7), coffee_daily, color='brown', alpha=0.7)
    axes[0, 1].set_title('Daily Coffee Totals')
    axes[0, 1].set_xlabel('Day')
    axes[0, 1].set_ylabel('Cups')
    axes[0, 1].set_xticks(range(7))
    axes[0, 1].set_xticklabels(days)
    
    # Phone pickups
    axes[0, 2].plot(range(7), phone_pickups, marker='o', color='blue', linewidth=2)
    axes[0, 2].set_title('Daily Phone Pickups')
    axes[0, 2].set_xlabel('Day')
    axes[0, 2].set_ylabel('Pickups')
    axes[0, 2].set_xticks(range(7))
    axes[0, 2].set_xticklabels(days)
    axes[0, 2].grid(True, alpha=0.3)
    
    # Steps heatmap
    im2 = axes[1, 0].imshow(steps_data, cmap='Greens', aspect='auto')
    axes[1, 0].set_title('Hourly Steps')
    axes[1, 0].set_xlabel('Day')
    axes[1, 0].set_ylabel('Hour (6 AM = 0)')
    axes[1, 0].set_xticks(range(7))
    axes[1, 0].set_xticklabels(days)
    plt.colorbar(im2, ax=axes[1, 0], label='Steps')
    
    # Daily steps
    axes[1, 1].bar(range(7), steps_daily, color='green', alpha=0.7)
    axes[1, 1].set_title('Daily Step Totals')
    axes[1, 1].set_xlabel('Day')
    axes[1, 1].set_ylabel('Steps')
    axes[1, 1].set_xticks(range(7))
    axes[1, 1].set_xticklabels(days)
    
    # Comparison of all activities (normalized)
    coffee_norm = coffee_daily / np.max(coffee_daily)
    phone_norm = phone_pickups / np.max(phone_pickups)
    steps_norm = steps_daily / np.max(steps_daily)
    
    axes[1, 2].plot(range(7), coffee_norm, marker='o', label='Coffee', linewidth=2)
    axes[1, 2].plot(range(7), phone_norm, marker='s', label='Phone', linewidth=2)
    axes[1, 2].plot(range(7), steps_norm, marker='^', label='Steps', linewidth=2)
    axes[1, 2].set_title('All Activities (Normalized)')
    axes[1, 2].set_xlabel('Day')
    axes[1, 2].set_ylabel('Normalized Activity Level')
    axes[1, 2].set_xticks(range(7))
    axes[1, 2].set_xticklabels(days)
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run all tracking examples"""
    print("DEAR DATA: Personal Observable Activity Tracking")
    print("=" * 50)
    print()
    print("This demonstrates tracking observable daily activities that can be measured:")
    print("🍵 Coffee consumption (cups per hour)")
    print("📱 Phone pickups (times per day)")
    print("👟 Steps taken (per hour)")
    print()
    
    # Run all tracking examples
    coffee_data, coffee_daily = track_coffee_consumption()
    phone_pickups = track_phone_pickups()
    steps_data, steps_daily = track_steps()
    
    print("\n" + "=" * 50)
    print("KEY INSIGHTS ABOUT ARRAY DIMENSIONS:")
    print("=" * 50)
    print()
    print("1D ARRAYS work well when:")
    print("  - You have one measurement per time period")
    print("  - Example: Daily totals, weekly summaries")
    print("  - Shape: (days,) or (weeks,)")
    print()
    print("2D ARRAYS work well when:")
    print("  - You want detailed time-of-day patterns")
    print("  - Example: Hourly measurements across multiple days")
    print("  - Shape: (hours, days) or (time_periods, days)")
    print()
    print("INDEXING & SLICING allows you to:")
    print("  - Extract specific time periods: data[morning_hours, :]")
    print("  - Extract specific days: data[:, weekdays]")
    print("  - Calculate averages: np.mean(data, axis=0) or axis=1")
    print("  - Find differences: data[-1] - data[0]")
    
    # Create visualizations
    visualize_all_data(coffee_data, coffee_daily, phone_pickups, steps_data, steps_daily)

if __name__ == "__main__":
    main()