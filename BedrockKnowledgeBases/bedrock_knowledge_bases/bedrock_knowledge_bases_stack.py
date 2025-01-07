from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    # aws_sqs as sqs,
)

from cdklabs.generative_ai_cdk_constructs import bedrock
from constructs import Construct

class BedrockKnowledgeBasesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        kb = bedrock.KnowledgeBase(self, "knowledgebase",
                                     embeddings_model=bedrock.BedrockFoundationModel.TITAN_EMBED_TEXT_V2_256,
                                     instruction="This knowledge base is for demo purposes, it returns the most relevent info",
                                     )
        
        docBucket = s3.Bucket(self, 'DockBucket')

        bedrock.S3DataSource(self, 'DataSource',
            bucket= docBucket,
            knowledge_base=kb,
            data_source_name='source',
            chunking_strategy= bedrock.ChunkingStrategy.FIXED_SIZE,
        )
        



        




