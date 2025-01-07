from django.db import models 

class YearQuerySet(models.QuerySet):
      def get_is_current_year(self):
        return self.filter(is_current_year=True).first()

class InstitutionQuerySet(models.QuerySet):
    def get_total_count(self):
        return self.count()
    
  
    # def get_income(self):
    #     return self.filter(type='income')
    
    # def get_total_expenses(self):
    #     return self.get_expenses().aggregate(
    #         total=models.Sum('amount')
    #     )['total'] or 0

    # def get_total_income(self):
    #     return self.get_income().aggregate(
    #         total=models.Sum('amount')
    #     )['total'] or 0