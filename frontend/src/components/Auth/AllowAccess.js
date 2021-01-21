import axiosInstance from "../auth/AxiosApi";



const AllowAccess = async (event) => {
    try {
        let response = await axiosInstance.get('/' + event + '/');
        const message = response.data.event;
        this.setState({
            message: message,
        });
        return message;
    }catch(error){
        console.log("Error: ", JSON.stringify(error, null, 4));
        throw error;
    }
}

export default AllowAccess