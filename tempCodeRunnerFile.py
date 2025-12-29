
# values = [1000, 2000, 3000, 2200, 3211, 9000, 6790]
# labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# # ------------------------------------------------
# # 1) Basic pie chart
# # ------------------------------------------------
# plt.pie(values, labels=labels)
# plt.title("Weekly Sales")
# plt.show()


# # ------------------------------------------------
# # 2) Pie chart with percentage display
# # ------------------------------------------------
# plt.pie(values, labels=labels, autopct='%1.1f%%')
# plt.title("Weekly Sales (%)")
# plt.show()


# # ------------------------------------------------
# # 3) Pie chart with start angle
# # ------------------------------------------------
# plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Weekly Sales (Rotated)")
# plt.show()


# # ------------------------------------------------
# # 4) Pie chart with exploded slices
# # ------------------------------------------------
# explode = [0, 0, 0, 0, 0.1, 0.2, 0]  # highlight Fri & Sat

# plt.pie(values, labels=labels, autopct='%1.1f%%', explode=explode)
# plt.title("Highlighted High Sales Days")
# plt.show()


# # ------------------------------------------------
# # 5) Pie chart with shadow effect
# # ------------------------------------------------
# plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)
# plt.title("Weekly Sales with Shadow")
# plt.show()


# # ------------------------------------------------
# # 6) Counter-clockwise pie chart
# # ------------------------------------------------
# plt.pie(values, labels=labels, autopct='%1.1f%%', counterclock=False)
# plt.title("Clockwise Pie Chart")
# plt.show()
