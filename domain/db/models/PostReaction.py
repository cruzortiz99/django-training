from django.db import models
from domain.db.models.Post import Post
from domain.db.models.Account import Account
import enum
from domain.db.models.BaseModel import BaseModel


class Reaction(enum.Enum):
    HAPPY = "happy"
    GLAD = "glad"
    EXCITED = "excited"
    SAD = "sad"
    AMAZE = "AMAZE"


class PostReaction(BaseModel):
    class Meta:
        db_table = "\"post_reaction\""
    post = models.ForeignKey(to=Post, on_delete=models.deletion.CASCADE,
                             null=False)
    reacted_by = models.ForeignKey(to=Account,
                                   on_delete=models.deletion.CASCADE,
                                   null=False)
    reaction = models.CharField(max_length=50, choices=[
        (Reaction.AMAZE.value, Reaction.AMAZE.name),
        (Reaction.EXCITED.value, Reaction.EXCITED.name),
        (Reaction.GLAD.value, Reaction.GLAD.name),
        (Reaction.HAPPY.value, Reaction.HAPPY.name),
        (Reaction.SAD.value, Reaction.SAD.name),
    ],  null=False, blank=False)
