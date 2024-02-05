from rest_framework import serializers
from .models import CalorieChart

class CalorieChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalorieChart
        fields = [
            'pk',
            'item_name',
            'is_cal_per_kg',
            'is_cal_per_liter',
            'is_cal_per_item',
            'calories',
            'description',
        ]

    def validate(self, data):
        is_cal_per_kg = data.get('is_cal_per_kg', False)
        is_cal_per_liter = data.get('is_cal_per_liter', False)
        is_cal_per_item = data.get('is_cal_per_item', False)

        # Check that exactly one of the three boolean fields is True
        if sum([is_cal_per_kg, is_cal_per_liter, is_cal_per_item]) != 1:
            raise serializers.ValidationError("Exactly one of is_cal_per_kg, is_cal_per_liter, is_cal_per_item must be True.")

        return data
