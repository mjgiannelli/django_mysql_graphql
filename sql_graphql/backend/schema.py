# schema describes the data models to provide to the graphQl server
# also creates resolves methods

import graphene
from graphene.types import mutation
# format our django object into a format that can be utilized by graphql
from graphene_django import DjangoObjectType

from .models import Employee

# these are the fields we have acess to. these are not the queries
class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('id', 'f_name', 'l_name')

# this is where you define type defs and resolvers
class Query(graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)

    # root is the entry point into the query
    # info is used to pass in information to run query

    def resolve_all_employees(root, info):
        return Employee.objects.all()

    # need to use .Field when returning only one instance of Employee
    employee = graphene.Field(EmployeeType, id=graphene.Int())

    def resolve_employee(root, info, id):
        return Employee.objects.get(id=id)

class AddEmployee(graphene.Mutation):

    class Arguments:
        f_name = graphene.String(required=True)
        l_name = graphene.String(required=True)
    
    employee = graphene.Field(EmployeeType)

    # adding a class method to build a function
    @classmethod
    def mutate(cls, root, info, f_name, l_name):
        employee = Employee(f_name=f_name, l_name=l_name)
        employee.save()
        return AddEmployee(employee=employee)

class UpdateEmployee(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        f_name = graphene.String(required=True)
        l_name = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, f_name, l_name, id):
        employee = Employee.objects.get(id=id)

        employee.f_name = f_name
        employee.l_name = l_name

        employee.save()

        return UpdateEmployee(employee=employee)

class Mutation(graphene.ObjectType):

    add_employee = AddEmployee.Field()
    update_employee = UpdateEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)