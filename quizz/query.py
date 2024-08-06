import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from .models import AddUser, Answer, Category, Questions, Quizes

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields=('id', 'name')
        

class AnswerType(DjangoObjectType):
    class Meta:
        model= Answer
        fields=('id','question','answer_text','is_right')
        
class QuestionsType(DjangoObjectType):
    class Meta:
        model= Questions
        fields=('title', 'quiz','technique')
        

class QuizesType(DjangoObjectType):
    class Meta:
        model= Quizes
        fields=('title', 'Category', 'date_created')
        
class AddUserType(DjangoObjectType):
    class Meta:
        model= AddUser
        fields=('id','username','password','is_active')        
class Queryy(graphene.ObjectType):
  
    # all_books = graphene.Field(BooksType, id=graphene.Int())
    all_questions =  graphene.List(QuestionsType)
    all_answers = graphene.List(AnswerType)
    all_categories = graphene.List(CategoryType)
    all_users = graphene.List(AddUserType)

    # def resolve_all_books(root, info, id ):
    #     return Books.objects.get(pk=id)

    def resolve_all_questions(root, info):
        return Questions.objects.all()
    
    def resolve_all_users(root, info):
        return AddUser.objects.all()

    def resolve_all_answers(root, info):
        return Answer.objects.filter(question=6)

    def resolve_all_categories(root, info):
        return Category.objects.all()
     
    # question = graphene.List(QuestionsType)
   
    # def resolve_allquestion(root, info):
    #      return Questions.objects.all()
           
        
class Query1(MeQuery,UserQuery, graphene.ObjectType):
    pass
    
