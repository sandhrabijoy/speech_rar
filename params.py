class Get_Params:

    vocab_size = 15000
    sequence_length = 20
    batch_size = 64
    
    num_heads = 2
    epochs = 10

    validation_split = 0.15
    embed_dim = 256
    latent_dim = 256

    model_path = "model.h5"
    begin_token = "[start]"
    end_token = "[end]"

    use_pretrained_model = False 



if __name__ == '__main__':

    config = Get_Params()